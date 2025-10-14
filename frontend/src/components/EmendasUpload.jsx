// frontend/src/components/EmendasUpload.jsx
import React, { useState } from "react";

function EmendasUpload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      setMessage("Por favor, selecione um ficheiro primeiro!");
      return;
    }
    setLoading(true);
    setMessage("A processar a planilha... Isto pode demorar alguns momentos.");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/uploads/emendas", {
        method: "POST",
        body: formData,
      });

      const json = await response.json();

      if (!response.ok) {
        throw new Error(json.detail || "Ocorreu um erro no servidor.");
      }

      setMessage(`✅ Sucesso! ${json.emendas_importadas} emendas foram importadas.`);
      if (onUploadSuccess) onUploadSuccess();
    } catch (err) {
      setMessage(`❌ Erro: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section>
      <h2>Importar Planilha de Emendas</h2>
      <p>Selecione um ficheiro .xlsx para importar os dados para o sistema.</p>
      <input 
        type="file" 
        accept=".xlsx"
        onChange={(e) => setFile(e.target.files[0])} 
        disabled={loading}
      />
      <button onClick={handleUpload} disabled={loading} style={{ marginLeft: "1rem" }}>
        {loading ? "A processar..." : "Enviar Planilha"}
      </button>
      {message && <p style={{ marginTop: '1rem', fontWeight: 'bold' }}>{message}</p>}
    </section>
  );
}

export default EmendasUpload;