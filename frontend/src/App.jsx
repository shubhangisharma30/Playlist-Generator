function App() {
  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>AI Playlist Generator</h1>

      <p>
        Paste a Spotify playlist and generate genre-based playlists using AI.
      </p>

      <input
        type="text"
        placeholder="Spotify Playlist URL"
        style={{ display: "block", marginBottom: "12px", width: "320px" }}
      />

      <input
        type="text"
        placeholder="Genres (e.g. Chill, Workout, Party)"
        style={{ display: "block", marginBottom: "12px", width: "320px" }}
      />

      <button disabled>Generate Playlists</button>
    </div>
  );
}

export default App;
