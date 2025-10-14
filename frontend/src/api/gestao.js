// frontend/src/api/gestao.js

const API_URL = "http://localhost:8000";

/**
 * Busca a lista de municípios da API.
 */
export async function fetchMunicipalities() {
  const response = await fetch(`${API_URL}/municipalities/`);
  if (!response.ok) {
    throw new Error(`Erro HTTP: ${response.status}`);
  }
  return await response.json();
}

/**
 * Busca a lista de emendas da API.
 */
export async function fetchEmendas() {
  const response = await fetch(`${API_URL}/emendas/`);
  if (!response.ok) {
    throw new Error(`Erro HTTP: ${response.status}`);
  }
  return await response.json();
}