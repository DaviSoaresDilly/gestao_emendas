import React, { useEffect, useState } from "react";
import { fetchMinioTest } from "../api/minio";

function MinioTest() {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchMinioTest()
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
    <section style={{ margin: "2rem 0" }}>
      <h2>Teste MinIO</h2>
      {loading && <p>Carregando...</p>}
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
    </section>
  );
}

export default MinioTest;
