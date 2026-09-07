#!/usr/bin/env python3
"""Build a single-file, completely offline game. No dependencies required."""
from pathlib import Path
root = Path(__file__).resolve().parent
src = root / 'src'
html = (src / 'shell.html').read_text()
css = (src / 'style.css').read_text()
js = '\n'.join((src / name).read_text() for name in ['engine.js', 'fallback.js', 'world.js', 'game.js', 'app.js'])
html = html.replace('/*__CSS__*/', css).replace('/*__JS__*/', js.replace('</script', '<\\/script'))
(root / 'index.html').write_text(html)
print(f'Built index.html: {len(html.encode()):,} bytes. No network dependencies.')
