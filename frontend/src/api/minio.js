const API_URL = "http://localhost:8000"; // Centralizado

/**
 * Testa a conexão com o MinIO via backend.
 * Retorna status, bucket e objetos no bucket.
 */
export async function fetchMinioTest() {
  const res = await fetch(`${API_URL}/minio/test`);
  if (!res.ok) throw new Error(`Erro HTTP: ${res.status}`);
  return await res.json();
}

/**
 * Faz upload de um arquivo para o MinIO via backend.
 * @param {File} file - Arquivo selecionado no input
 */
export async function uploadToMinio(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_URL}/minio/upload`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) throw new Error(`Erro HTTP: ${res.status}`);
  return await res.json();
}
