# THANE RUSH
## Lakeside to Hillside

An original, dependency-free 3D arcade driving game inspired by Upvan Lake,
Yeoor Hills, Pokhran Road No. 2, Neelkanth Heights and Vasant Vihar in Thane.

**Play:** open `index.html` in a desktop browser, then press **LET'S DRIVE**.
The distributed `Thane_Rush.html` file is identical to `index.html`.
There is no installation, account, package download, or server requirement for the game.
Touch controls are included for mobile-sized browsers. Opening a local HTML file
on a phone depends on the phone's browser and file-opening restrictions; a static
web host avoids those restrictions.

## The game

The 5.1 km route is a fictional, closed course with six sectors:
Pokhran Road No. 2 → Upvan Lake → Yeoor Hill Climb → Yeoor Descent →
Neelkanth Heights → Vasant Vihar → finish.

The terrain, layout, architecture and connections are artistic approximations,
not a survey, navigation map or representation of current road access.

### Choose your run

| Mode | What changes |
| --- | --- |
| Sunset sprint | Three racing rivals, traffic, checkpoint timer and a finish-line score. |
| Monsoon madness | Rain, lower grip and speed ceiling, heavier traffic and a more generous checkpoint timer. |
| Sunday drive | No time limit; keep exploring repeated laps, then finish from the pause menu. |

### Choose your ride

| Ride | Personality |
| --- | --- |
| Lakeside GT | Balanced speed and handling. |
| Yeoor Rally | More grip for the hill sections and wet roads. |
| Rickshaw Rocket | Playful handling and 25% extra pickup/overtake points. |

Traffic includes cars, rickshaws and buses. Use the horn to encourage nearby
traffic ahead to pull aside. Dodge potholes and cones; collect floating chai cups;
chain clean close overtakes; drift to recharge boost. Scenery includes the lake,
promenade, a pavilion, boats, stalls, road signs, wooded hills and apartment towers.

## Controls

Auto throttle is **on by default**. You can concentrate on steering and braking.

| Action | Keyboard |
| --- | --- |
| Steer | A / D or left / right arrows |
| Accelerate | W or up arrow |
| Brake | S or down arrow |
| Boost | Hold Space |
| Drift | Hold Shift while steering |
| Yield horn | H |
| Auto throttle | T |
| Chase / road camera | C |
| Pause / resume | P or Escape |
| Restart | R |
| Start from menu | Enter |
| Sound / music | M / N |
| Fullscreen | F, where the browser supports it |

On touch screens, hold the onscreen steering arrows and pedals. A **GAS** pedal
appears when auto throttle is turned off. Pause contains graphics, camera,
auto-throttle and music settings. Multi-pointer input permits steering and
boosting together. Losing browser focus pauses the race.

## Scoring

* Chai: 250 base points and 35 percentage points of boost, capped at 100%.
* Clean close overtake: 100 base points, multiplied by the current combo.
* Drifting: style points and boost regeneration while on the road.
* Clean sector: 500 points; a sector with contact: 200 points.
* Other contact: −180 points; pothole: −80 points. Scores cannot go below zero.
* Completed race: 5,000 points plus remaining-time and position bonuses.

Finishing first with fewer than seven contacts earns gold. Finishing first or
second otherwise earns silver; the remaining completed placements earn bronze.
Sunday drive awards an Explorer result. A failed timed run does not receive a
completion bonus or a saved record.

Records and settings are stored in **this browser**, when local storage is
available. There is no global leaderboard, backend, sign-in or telemetry.
Private browsing, storage restrictions or clearing browser data may prevent or
remove saved records. Moving the file or using a different hosted origin may
also change which local records are accessible.

## Running and editing the source

The shipped HTML is already built. No build step is needed to play it.

To rebuild after editing the readable source files:

```sh
python3 build.py
```

For optional local HTTP serving:

```sh
python3 -m http.server 8080
# Open http://localhost:8080
```

For simulation tests (Node.js; no npm dependencies):

```sh
nodetests/simulation.test.js
```

Optional UI regression tests use Python Playwright and a Chromium executable.
The checked-in runner uses `/usr/bin/chromium`; change that path for another
installation. This optional test dependency is **not needed by the game**.

```sh
python3tests/browser.test.py desktop
python3tests/browser.test.py portrait
python3tests/browser.test.py landscape
```

### Project layout

```text
index.html                  Ready-to-play single-file build
build.py                    Python standard-library bundler
src/shell.html              Accessible UI and game screens
src/style.css               Desktop and responsive touch layouts
src/engine.js               Vector math, mesh construction and WebGL renderer
src/fallback.js             Software 3D renderer with a per-pixel depth buffer
src/world.js                Original procedural scenery and vehicle geometry
src/game.js                 Physics, traffic AI, scoring, sound and storage
src/app.js                  UI, controls, cameras, render loop and persistence
tests/                     Regression tests and actual test results
screenshots/                Captures from browser layout and scene checks
QA.md                       Test coverage and limitations
PUBLISHING.md               Hosting contract and publishing status
LICENSE                     MIT license for the original code/assets
```

`src/` does not use a framework or third-party runtime library. WebGL is attempted
first; when it cannot initialize, the game falls back to an original Canvas
software renderer. All meshes, effects, labels, icons, engine/horn effects and
music are generated locally. No fonts, textures, models, audio or JavaScript are
fetched from a CDN.

## Publishing status

**No live ChatGPT Sites deployment was created.** A ChatGPT Sites publishing
action was not available in the creation session. The deliverable is a playable
HTML file and its source, not a public site URL. See `PUBLISHING.md` for the static
hosting contract. This README does not assume that a particular Sites account
supports importing this file.

## Credits and boundaries

Concept reference, inspected for gameplay inspiration:
https://orr-rush-bengaluru.ravitheja.chatgpt.site/

Geographic inspiration:
https://maharashtratourism.gov.in/districts/thane/

No reference-game code or assets are included. All game geometry, interface,
code, sound effects and synthesized music were created for this project.

All racing is fictional and stays in the game. Road rules, current conditions,
entry restrictions and wildlife movements are not represented. Pedestrians and
boats are scenery, not targets.
