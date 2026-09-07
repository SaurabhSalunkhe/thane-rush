# Publishing contract

## Actual status

The project is built, playable and packaged. It has **not** been published to
ChatGPT Sites, and no public game URL has been issued. The creation session did
not expose a ChatGPT Sites publishing action. This package does not contain
credentials or a script that can publish to that service.

## Static host requirements

* Entry document: `index.html`.
* Content type: `text/html; charset=utf-8`.
* Build command: none for the shipped HTML; `python3 build.py` only after source edits.
* Runtime: a browser with JavaScript and Canvas. WebGL is preferred, with a Canvas fallback.
* Server functions, database, environment variables and third-party runtime assets: none.
* Public path: any directory where the entry HTML is served. There are no relative asset paths.
* HTTPS is preferred for browser clipboard/fullscreen features. Core gameplay is offline-capable.

The HTML contains inline styles and scripts. A host must permit its inline
JavaScript/CSS, or the source can be adapted into separately hosted assets with a
matching Content Security Policy. Sandboxed frames must allow scripts; persistent
scores require usable local storage. Fullscreen and clipboard support are optional.

A publisher with access to the intended hosting service can use this completed
static entry point; the game does not need to be rewritten. File-import support
and publication permissions must be checked in that publishing environment.
No specific ChatGPT Sites import workflow was verified during creation.
