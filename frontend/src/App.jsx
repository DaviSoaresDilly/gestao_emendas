import React, { useState } from "react";
import MinioTest from "./components/MinioTest";
import MinioUpload from "./components/MinioUpload";

function App() {
  const [refreshKey, setRefreshKey] = useState(0);

  return (
    <main className="container">
      <header>
        <h1>Frontend rodando com Vite 🚀</h1>
        <p>Agora você pode conectar com o backend FastAPI.</p>
      </header>

      <section>
        <MinioUpload onUploadSuccess={() => setRefreshKey((k) => k + 1)} />
        <MinioTest key={refreshKey} />
      </section>
    </main>
  );
}

export default App;
