// frontend/src/components/pages/EmendasList.jsx

import React from "react";
import { fetchEmendas } from "../../api/gestao";

// Hook personalizado para buscar os dados
function useEmendas(refreshKey) {
  const [data, setData] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState(null);

  React.useEffect(() => {
    setLoading(true);
    fetchEmendas()
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [refreshKey]); // A lista será atualizada sempre que a refreshKey mudar

  return { data, loading, error };
}

function EmendasList({ refreshKey }) {
  const { data: emendas, loading, error } = useEmendas(refreshKey);

  if (loading) return <p>A carregar emendas...</p>;
  if (error)
    return (
      <p style={{ color: "red" }}>Erro ao buscar dados: {error.message}</p>
    );

  return (
    <section className="emendas-list">
      <h2>Lista de Emendas Importadas</h2>
      {emendas.length === 0 ? (
        <p>Nenhuma emenda encontrada. Tente importar uma planilha.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Ano</th>
              <th>Nº Indicação</th>
              <th>Município</th>
              <th>Beneficiário</th>
              <th>Status</th>
              <th>Valor Indicado</th>
              <th>Valor Pago</th>
            </tr>
          </thead>
          <tbody>
            {emendas.map((emenda) => (
              <tr key={emenda.id}>
                <td>{emenda.ano}</td>
                <td>{emenda.numero_indicacao}</td>
                <td>{emenda.municipality.name}</td>
                <td>{emenda.beneficiario_nome || "-"}</td>
                <td>{emenda.status.nome}</td>
                <td>
                  {new Intl.NumberFormat("pt-BR", {
                    style: "currency",
                    currency: "BRL",
                  }).format(emenda.valor_indicado)}
                </td>
                <td>
                  {/* Mostra o valor pago ou um traço se não houver */}
                  {emenda.valor_pago
                    ? new Intl.NumberFormat("pt-BR", {
                        style: "currency",
                        currency: "BRL",
                      }).format(emenda.valor_pago)
                    : "-"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </section>
  );
}

export default EmendasList;
