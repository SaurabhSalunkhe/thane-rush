# Thane Rush

An original 3D arcade driving game inspired by Upvan Lake, Yeoor Hills, and the streets of Thane.

Play it at [thane-rush.saurabhsalunkhe.chatgpt.site](https://thane-rush.saurabhsalunkhe.chatgpt.site).

## Local development

```sh
npm install
npm run dev
```

The readable, dependency-free game source lives in [`game/`](game/). The ready-to-play single-file build is served as [`public/game.html`](public/game.html) inside the Sites wrapper.

## Tests

```sh
npm run build
node game/tests/simulation.test.js
```

## License

MIT. See [`LICENSE`](LICENSE).
