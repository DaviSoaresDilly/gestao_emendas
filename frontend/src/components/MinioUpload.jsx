import React, { useState } from "react";
import { uploadToMinio } from "../api/minio";

function MinioUpload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    if (!file) return setMessage("Selecione um arquivo primeiro!");
    try {
      const json = await uploadToMinio(file);
      if (json.status === "ok") {
        setMessage(`✅ Arquivo "${json.filename}" enviado com sucesso!`);
        if (onUploadSuccess) onUploadSuccess();
      } else {
        setMessage(`❌ Erro: ${json.details}`);
      }
    } catch (err) {
      setMessage(`❌ Erro: ${err.message}`);
    }
  };

  return (
    <section style={{ margin: "2rem 0" }}>
      <h2>Upload de Arquivo</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload} style={{ marginLeft: "1rem" }}>
        Enviar
      </button>
      {message && <p>{message}</p>}
    </section>
  );
}

export default MinioUpload;
