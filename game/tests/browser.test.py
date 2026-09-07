"""Chromium UI regression/screenshot checks; requires optional playwright for Python.
Uses set_content because this build environment blocks browser URL navigation.
Run: python tests/browser.test.py [desktop|portrait|landscape]
"""
import asyncio, json, sys, time
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
TARGET=sys.argv[1] if len(sys.argv)>1 else 'desktop'
HTML=(ROOT/'index.html').read_text().replace("if(new URLSearchParams(location.search).has('test'))",'if(true)')
async def main():
 results=[];errors=[];requests=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
  mobile=TARGET!='desktop'; width,height={'desktop':(1440,900),'portrait':(390,844),'landscape':(844,390)}[TARGET]
  context=await browser.new_context(viewport={'width':width,'height':height},device_scale_factor=1,is_mobile=mobile,has_touch=mobile)
  page=await context.new_page();page.on('pageerror',lambda e:errors.append(str(e)));page.on('request',lambda r:requests.append(r.url))
  await page.set_content(HTML,wait_until='load');await page.wait_for_function('window.thaneRush?.initialized',timeout=40000)
  await page.wait_for_timeout(200)
  def check(name,ok,detail=None):
   results.append({'name':name,'passed':bool(ok),'detail':detail}); print(('PASS' if ok else 'FAIL'),TARGET,name,detail or '',flush=True)
  bounds=await page.evaluate('''()=>({width:innerWidth,height:innerHeight,bodyWidth:document.body.scrollWidth,menuWidth:document.querySelector('#menu').scrollWidth,menuHeight:document.querySelector('#menu').scrollHeight,menuClientHeight:document.querySelector('#menu').clientHeight,start:document.querySelector('#startButton').getBoundingClientRect().toJSON(),touch:matchMedia('(pointer:coarse)').matches})''')
  check('No horizontal menu overflow',bounds['bodyWidth']<=width and bounds['menuWidth']<=width,bounds)
  await page.locator('#startButton').scroll_into_view_if_needed()
  await page.screenshot(path=str(ROOT/'screenshots'/f'{TARGET}-menu.png'))
  check('Start button can be reached',await page.locator('#startButton').is_visible())
  # Modal access and closing; change ride and mode before starting.
  await page.click('#aboutButton');check('About dialog opens',await page.locator('#infoOverlay').is_visible());await page.click('#closeInfo')
  await page.click('[data-car="rally"]');await page.click('[data-mode="monsoon"]')
  check('Monsoon chooses rain and rally car',await page.evaluate("thaneRush.weather()==='rain' && thaneRush.car==='rally' && document.querySelector('#weatherButton').disabled"))
  await page.click('[data-car="gt"]');await page.click('[data-mode="rush"]');await page.click('#startButton')
  check('Start enters countdown',await page.evaluate("thaneRush.game.state==='countdown'"))
  await page.evaluate('window.__THANE_TEST__.step(3.3)')
  check('Countdown reaches running',await page.evaluate("thaneRush.game.state==='running' && !document.querySelector('#hud').hidden"))
  await page.click('#dismissTutorial')
  # Drive for deterministic steps using normal keyboard input object.
  await page.evaluate('''()=>{let a=thaneRush; a.game.traffic=[];a.game.rivals=[];a.game.hazards=[];a.game.items=[];__THANE_TEST__.teleport(920,-1.65,45);a.game.time=12;}''')
  before=await page.evaluate('thaneRush.game.x')
  if mobile:
   box=await page.locator('[data-touch="right"]').bounding_box();await page.mouse.move(box['x']+box['width']/2,box['y']+box['height']/2);await page.mouse.down()
   check('Touch right input registered',await page.evaluate('thaneRush.touch.right===true'))
   await page.evaluate('''()=>{for(let i=0;i<24;i++)thaneRush.game.step(1/120,thaneRush.input());}''')
   await page.mouse.up()
  else:
   await page.keyboard.down('ArrowRight');await page.evaluate('''()=>{for(let i=0;i<24;i++)thaneRush.game.step(1/120,thaneRush.input());}''');await page.keyboard.up('ArrowRight')
  check('Steering changes lane',await page.evaluate('thaneRush.game.x')>before)
  await page.click('#pauseButton');snapshot=await page.evaluate('__THANE_TEST__.snapshot()');await page.wait_for_timeout(150)
  check('Pause freezes physics',await page.evaluate('thaneRush.game.time')==snapshot['time'])
  check('Pause controls visible',await page.locator('#resumeButton').is_visible())
  await page.click('#pauseCam');check('Camera can change',await page.evaluate('thaneRush.cameraMode===1'))
  await page.click('#pauseCam');await page.click('#resumeButton');check('Resume returns to game',await page.evaluate("thaneRush.game.state==='running'"))
  if mobile:
   await page.evaluate('thaneRush.toggleAuto()')
   check('Manual touch mode reveals GAS pedal',await page.locator('#touchGas').is_visible())
   box=await page.locator('#touchGas').bounding_box();await page.mouse.move(box['x']+box['width']/2,box['y']+box['height']/2);await page.mouse.down()
   check('GAS pedal produces throttle input',await page.evaluate('thaneRush.input().throttle===true'))
   await page.mouse.up()
   await page.evaluate('thaneRush.toggleAuto()')
  # Stage the lake, with simulation frozen for an unambiguous screenshot.
  await page.evaluate('''()=>{let a=thaneRush;__THANE_TEST__.teleport(980,-1.65,45);a.game.time=18;a.game.state='paused';a.updateHUD();a.bannerUntil=0;a.toastUntil=0;}''')
  await page.wait_for_timeout(120);await page.screenshot(path=str(ROOT/'screenshots'/f'{TARGET}-upvan.png'))
  if mobile:
   for name in ['left','right','brake','boost','drift']:
    box=await page.locator(f'[data-touch="{name}"]').bounding_box()
    check(f'Touch {name} on screen',box and box['x']>=0 and box['y']>=0 and box['x']+box['width']<=width+1 and box['y']+box['height']<=height+1,box)
  if TARGET=='desktop':
   await page.evaluate('''()=>{__THANE_TEST__.teleport(2180,-1.65,48);thaneRush.updateHUD();}''');await page.wait_for_timeout(120);await page.screenshot(path=str(ROOT/'screenshots/desktop-yeoor.png'))
   await page.evaluate('''()=>{let a=thaneRush;a.selectMode('monsoon');a.game.mode='monsoon';__THANE_TEST__.teleport(1280,-1.65,40);a.updateHUD();}''');await page.wait_for_timeout(120);await page.screenshot(path=str(ROOT/'screenshots/desktop-monsoon.png'))
   await page.evaluate('''()=>{let a=thaneRush;a.selectMode('rush');a.settings.weather='night';__THANE_TEST__.teleport(4150,-1.65,43);a.updateHUD();}''');await page.wait_for_timeout(120);await page.screenshot(path=str(ROOT/'screenshots/desktop-night.png'))
  await page.evaluate('''()=>{let a=thaneRush;a.game.state='running';a.game.time=105;a.game.s=a.route.length-.05;a.game.zone=5;a.game.score=8800;a.game.speed=40;a.game.step(.02,{throttle:true});}''')
  check('Finish displays result sheet',await page.locator('#resultsOverlay').is_visible())
  check('Result not blank',len(await page.locator('#finalScore').inner_text())>0)
  await page.screenshot(path=str(ROOT/'screenshots'/f'{TARGET}-result.png'))
  await page.click('#garageButton');check('Garage returns to menu',await page.evaluate("thaneRush.game.state==='menu'"))
  await page.click('[data-mode="free"]');await page.click('#startButton');await page.evaluate('__THANE_TEST__.step(3.3)');await page.click('#pauseButton')
  check('Sunday drive offers finish-drive action',await page.locator('#endDriveButton').is_visible())
  await page.click('#endDriveButton');check('Sunday drive finishes as Explorer',await page.locator('#medalValue').inner_text()=='EXPLORER')
  check('No uncaught browser errors',not errors,errors)
  check('No runtime network requests',not requests,requests)
  renderer=await page.evaluate("({software:!!thaneRush.software,width:thaneRush.R.canvas.width,height:thaneRush.R.canvas.height})")
  data={'target':TARGET,'renderer':renderer,'passed':sum(t['passed'] for t in results),'total':len(results),'tests':results,'errors':errors,'requests':requests}
  (ROOT/'tests'/f'browser-{TARGET}-results.json').write_text(json.dumps(data,indent=2))
  await browser.close()
  print(json.dumps({k:v for k,v in data.items() if k!='tests'},indent=2))
  if data['passed']!=data['total']:raise SystemExit(1)
asyncio.run(main())
