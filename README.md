````markdown
# 🚀 Projeto Fullstack: React + FastAPI + MinIO

[![React](https://img.shields.io/badge/React-18.2.0-blue?logo=react)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![MinIO](https://img.shields.io/badge/MinIO-RELEASE-orange?logo=minio)](https://min.io/)
[![Docker](https://img.shields.io/badge/Docker-24.0.5-blue?logo=docker)](https://www.docker.com/)

---

## 📑 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Configuração](#configuração)
- [Como Rodar](#como-rodar)
- [Fluxo de Uso](#fluxo-de-uso)
- [Endpoints Principais](#endpoints-principais)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Testes](#testes)
- [Problemas Comuns](#problemas-comuns)
- [Contribuição](#contribuicao)
- [Licença](#licenca)
- [Contato](#contato)

---

## 📝 Sobre o Projeto

Este projeto é um template fullstack para gestão de emendas parlamentares, com upload de arquivos via MinIO, frontend em React (Vite) e backend em FastAPI. O objetivo é facilitar o armazenamento e consulta de documentos de forma segura e escalável.

---

## 🛠 Tecnologias Utilizadas

- **Frontend:** [React](https://react.dev/), [Vite](https://vitejs.dev/)
- **Backend:** [Python](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com/)
- **Armazenamento:** [MinIO](https://min.io/) (compatível S3)
- **Banco de dados:** [PostgreSQL](https://www.postgresql.org/)
- **Containerização:** [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)

---

## ⚡ Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Navegador moderno

---

## 🔧 Configuração

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo (veja também `.env.example`):

```env
# MinIO
MINIO_HOST=minio
MINIO_PORT=9000
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=minioadmin

# PostgreSQL
DB_HOST=postgres
DB_PORT=5432
DB_NAME=gestao_emendas
DB_USER=postgres
DB_PASS=postgres

# Backend
BACKEND_PORT=8000

# Frontend
FRONTEND_PORT=3000
```

---

## 🏃 Como Rodar

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd gestao_emendas
   ```

2. Suba os containers:

   ```bash
   docker compose up --build -d
   ```

   Ou, no Windows PowerShell:

   ```powershell
   ./run_dev.ps1
   ```

3. Acesse os serviços:
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend: [http://localhost:8000](http://localhost:8000)
   - MinIO WebUI: [http://localhost:9001](http://localhost:9001)  
     Usuário: `minioadmin` | Senha: `minioadmin`
   - PostgreSQL: porta `5432`

---

## 🖥️ Fluxo de Uso

1. Acesse o frontend e faça login (se aplicável).
2. Clique em **Teste MinIO** para listar arquivos do bucket.
3. Faça upload de arquivos usando o botão **Upload de arquivo**.
4. Os arquivos enviados ficam disponíveis no MinIO e podem ser listados no frontend.

![Exemplo de tela do frontend](docs/screenshot.png) <!-- Adicione uma imagem real do seu projeto aqui -->

---

## 🔗 Endpoints Principais

- **GET /**  
  Verifica se o backend está ativo.

  ```json
  { "message": "Backend rodando 🚀" }
  ```

- **GET /minio/test**  
  Lista objetos do bucket MinIO.

  ```json
  { "status": "ok", "bucket": "emendas-bucket", "objects": ["hello.txt"] }
  ```

- **POST /minio/upload**  
  Envia arquivo para o MinIO.
  ```bash
  curl -X POST http://localhost:8000/minio/upload -F "file=@/caminho/para/seu/arquivo.txt"
  ```

---

## 📂 Estrutura do Projeto

```
.
├── app/                  # Código compartilhado (opcional)
│   └── main.py
├── backend/              # Backend FastAPI
│   ├── app/
│   │   └── main.py
│   ├── Dockerfile.dev
│   ├── Dockerfile.prod
│   └── requirements.txt
├── frontend/             # Frontend React + Vite
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   └── MinioTest.jsx
│   │   ├── index.css
│   │   └── index.jsx
│   ├── Dockerfile.dev
│   ├── Dockerfile.prod
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml
├── .env
├── .env.example
├── .gitignore
├── run_dev.ps1
└── README.md
```

---

## 🧪 Testes

- Para rodar apenas o frontend localmente:
  ```bash
  cd frontend
  npm install
  npm run dev
  ```
- Para rodar apenas o backend localmente:
  ```bash
  cd backend
  pip install -r requirements.txt
  uvicorn app.main:app --reload
  ```
- Teste os endpoints usando ferramentas como [Postman](https://www.postman.com/) ou `curl`.

---

## 🛠️ Problemas Comuns

- **Failed to fetch:**  
  Verifique se o backend está rodando e se o CORS está habilitado no FastAPI.
- **MinIO não inicializa:**  
  Confira as variáveis de ambiente e se as portas estão livres.
- **Banco de dados não conecta:**  
  Certifique-se que o serviço PostgreSQL está ativo e as credenciais estão corretas.

---

## 🤝 Contribuição

1. Fork este repositório
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas alterações (`git commit -m 'feat: nova feature'`)
4. Push para o branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📫 Contato

- Desenvolvedor: **Davi Soares Dilly**
- E-mail: [davi.cyebrjatico@gmail.com](mailto:davi.cyebrjatico@gmail.com)

---
````
