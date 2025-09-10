import React, { useEffect, useState } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/minio/test")
      .then((res) => res.json())
      .then((json) => {
        setData(json);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1>Frontend rodando com Vite 🚀</h1>
      <p>Agora você pode conectar com o backend FastAPI.</p>

      <hr style={{ margin: "2rem 0" }} />

      <h2>Teste MinIO</h2>
      {loading && <p>Carregando dados do MinIO...</p>}
      {error && <p style={{ color: "red" }}>Erro: {error}</p>}
      {data && (
        <div>
          <p>Bucket: {data.bucket}</p>
          <p>Status: {data.status}</p>
          <ul>
            {data.objects.map((obj) => (
              <li key={obj}>{obj}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
