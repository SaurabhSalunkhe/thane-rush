export default function Home() {
  return (
    <main className="game-shell">
      <iframe
        className="game-frame"
        src="/game.html"
        title="Thane Rush — Lakeside to Hillside"
        allow="autoplay; fullscreen"
      />
      <noscript>
        <p>Thane Rush needs JavaScript enabled to play.</p>
      </noscript>
    </main>
  );
}
