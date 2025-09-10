import React, { useEffect, useState } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [file, setFile] = useState(null);
  const [uploadMsg, setUploadMsg] = useState("");

  // URL do backend no Docker Compose
  const BACKEND_URL = "http://backend:8000";

  const fetchMinio = () => {
    setLoading(true);
    fetch(`${BACKEND_URL}/minio/test`)
      .then((res) => res.json())
      .then((json) => {
        setData(json);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchMinio();
  }, []);

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch(`${BACKEND_URL}/minio/upload`, {
        method: "POST",
        body: formData,
      });
      const json = await res.json();
      if (json.status === "ok") {
        setUploadMsg(`Arquivo "${json.filename}" enviado com sucesso!`);
        fetchMinio(); // Atualiza lista de arquivos
      } else {
        setUploadMsg(`Erro: ${json.details}`);
      }
    } catch (err) {
      setUploadMsg(`Erro: ${err.message}`);
    }
  };

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

      <hr style={{ margin: "2rem 0" }} />
      <h2>Upload de arquivo</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload} style={{ marginLeft: "1rem" }}>
        Enviar
      </button>
      {uploadMsg && <p>{uploadMsg}</p>}
    </div>
  );
}

export default App;
