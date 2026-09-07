# QA record — 7 September 2026

## Results

**28/28 simulation checks passed.**
**70/70 browser UI checks passed** across desktop 1440×900, portrait 390×844,
and landscape 844×390 viewports.

Simulation tests cover the continuous closed route; countdown; acceleration,
steering, braking and speed ceilings; boost and recharge lock; drift recharge;
traffic yield and horn cooldown; collisions; potholes; one-time pickups; the
rickshaw reward bonus; clean overtakes; checkpoints; pause; timeout; finish;
endless laps; rain behavior; deterministic traffic; and mock storage persistence.

Two automated test drivers completed full courses using normal steering,
acceleration, boost and horn inputs, without teleports or modified race physics.
The test driver's driving policy is in `tests/simulation.test.js`.

| Full simulation | Result | Time | Peak speed |
| --- | --- | --- | --- |
| rush / gt | Completed, position 1 | 86.28 seconds | 277 km/h |
| monsoon / rally | Completed, position 1 | 98.58 seconds | 244 km/h |

Browser checks cover initialization, horizontal overflow, reachable start button,
About modal, ride/mode changes, countdown, keyboard/pointer steering, pause and
resume, camera toggle, on-screen touch control placement, manual GAS pedal,
result screen, garage return and finishing Sunday Drive. No uncaught page errors
or runtime network requests were observed in the passing checks.

## Test environment and limitations

Tests used headless Chromium in the creation environment. WebGL could not
initialize in this environment, so browser graphics tests and screenshots used
the game's genuine software 3D fallback. The WebGL renderer is implemented but
**was not GPU-rendered or validated on a physical graphics device here**.

Browser URL navigation, including localhost and file URLs, was blocked by the
creation environment. UI tests load the identical built inline HTML with
Playwright `set_content`; production code is unchanged except that the optional
query-string test API is enabled by the test harness. This is not a direct
file-opening or deployed-host test.

Phone layouts were emulated with coarse-pointer/mobile viewports; they were not
tested on physical phones. UI pointer holds used real browser pointer events.
No claim of Safari, Firefox or physical iOS/Android validation is made.

Browser local storage was restricted on the test document's opaque origin.
The UI handled this and reported unavailable persistence rather than claiming
a score was saved. Save/load logic was tested independently with a storage mock.
Clipboard and fullscreen availability depend on browser permissions and were not
certified across devices. No multiplayer or online leaderboard exists.

Scenery screenshots intentionally use controlled in-game positions and freeze
physics for comparison. They are not records of a full human playthrough.

## Files

Detailed machine-readable results are in `tests/*-results.json`.
Reproduction instructions are in `README.md`. The single-file distribution and
source `index.html` are byte-identical. No live hosting test or ChatGPT Sites
publication was performed.
