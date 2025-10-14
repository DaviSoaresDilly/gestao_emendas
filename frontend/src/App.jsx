// frontend/src/App.jsx
import React, { useState } from "react";
import EmendasUpload from "./components/EmendasUpload";
import EmendasList from "./components/pages/EmendasList";

function App() {
  const [refreshKey, setRefreshKey] = useState(0);

  // Esta função será chamada pelo EmendasUpload após o sucesso,
  // para forçar a atualização da lista de emendas.
  const handleSuccess = () => {
    setRefreshKey((prevKey) => prevKey + 1);
  };

  return (
    <main className="container">
      <header>
        <h1>Gestão de Emendas Parlamentares 🚀</h1>
      </header>

      <EmendasUpload onUploadSuccess={handleSuccess} />

      {/* A key={refreshKey} é um truque para forçar o React a recriar
          o componente EmendasList, fazendo com que ele busque os novos dados. */}
      <EmendasList key={refreshKey} />
    </main>
  );
}

export default App;
