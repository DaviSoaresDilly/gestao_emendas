---

# 🚀 Projeto Fullstack: Gestão de Emendas (React + FastAPI + MinIO + PostgreSQL)

[![React](https://img.shields.io/badge/React-18.2.0-blue?logo=react)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![MinIO](https://img.shields.io/badge/MinIO-RELEASE-orange?logo=minio)](https://min.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue?logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-24.0.5-blue?logo=docker)](https://www.docker.com/)

---

## 📑 Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Configuração](#-configuração)
- [Como Rodar](#-como-rodar)
- [Fluxo de Uso](#-fluxo-de-uso)
- [Endpoints Principais](#-endpoints-principais)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Testes](#-testes)
- [Problemas Comuns](#-problemas-comuns)
- [Contribuição](#-contribuição)
- [Licença](#-licença)
- [Contato](#-contato)

---

## 📝 Sobre o Projeto

Este projeto é um **template fullstack** para gestão de emendas parlamentares, com:

- Upload e armazenamento de arquivos via **MinIO** (compatível com S3).
- Frontend em **React (Vite)**.
- Backend em **FastAPI (Python)**.
- Banco de dados relacional em **PostgreSQL**.

O objetivo é fornecer uma base moderna, escalável e segura para aplicações que demandam **persistência de documentos, integração com API e banco de dados**.

---

## 🛠 Tecnologias Utilizadas

- **Frontend:** [React](https://react.dev/), [Vite](https://vitejs.dev/)
- **Backend:** [Python](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com/)
- **Armazenamento:** [MinIO](https://min.io/)
- **Banco de Dados:** [PostgreSQL](https://www.postgresql.org/)
- **Containerização:** [Docker](https://www.docker.com/) + [Docker Compose](https://docs.docker.com/compose/)

---

## ⚡ Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Navegador moderno

---

## 🔧 Configuração

Crie um arquivo `.env` na raiz do projeto com suas credenciais (veja também `.env.example`):

```
# Banco de dados
DB_HOST=postgres
DB_PORT=5432
DB_NAME=gestao_emendas
DB_USER=postgres
DB_PASS=postgres

# Backend
BACKEND_PORT=8000

# Frontend
FRONTEND_PORT=3000

# MinIO
MINIO_HOST=minio
MINIO_PORT=9000
MINIO_ROOT_USER=<seu_usuario>
MINIO_ROOT_PASSWORD=<sua_senha>
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

   Ou no Windows PowerShell:

   ```powershell
   ./run_dev.ps1
   ```

3. Acesse os serviços:

   - **Frontend:** [http://localhost:3000](http://localhost:3000)
   - **Backend:** [http://localhost:8000](http://localhost:8000)
   - **MinIO WebUI:** [http://localhost:9001](http://localhost:9001)
   - **PostgreSQL:** porta `5432`

---

## 🖥️ Fluxo de Uso

1. Acesse o **frontend**.
2. Clique em **Teste MinIO** → lista os arquivos disponíveis no bucket.
3. Use o **Upload de Arquivo** para enviar documentos.
4. Confirme no **MinIO WebUI** que os arquivos foram armazenados.

---

## 🔗 Endpoints Principais

- **GET /**
  Verifica se o backend está ativo.

  ```json
  { "message": "Backend rodando 🚀" }
  ```

- **GET /minio/test**
  Lista objetos no bucket MinIO.

  ```json
  { "status": "ok", "bucket": "emendas-bucket", "objects": ["hello.txt"] }
  ```

- **POST /minio/upload**
  Faz upload de arquivo para o MinIO.

  ```bash
  curl -X POST http://localhost:8000/minio/upload -F "file=@/caminho/arquivo.txt"
  ```

---

## 📂 Estrutura do Projeto

```

├── backend/
│   ├── app/
│   │   ├── routers/
│   │   │   ├── minio.py            # Endpoints para MinIO
│   │   │   └── municipalities.py   # Endpoints para municípios
│   │   ├── crud.py                 # Lógica de acesso ao banco
│   │   ├── database.py             # Configuração do banco de dados
│   │   ├── main.py                 # Ponto de entrada do FastAPI
│   │   ├── models.py               # Modelos do banco de dados
│   │   └── schemas.py              # Validação de dados da API
│   ├── Dockerfile.dev              # Dockerfile para desenvolvimento
│   ├── Dockerfile.prod             # Dockerfile para produção
│   ├── requirements-dev.txt        # Dependências de desenvolvimento
│   └── requirements-prod.txt       # Dependências de produção
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── minio.js            # Integração com MinIO
│   │   ├── components/
│   │   │   ├── MinioTest.jsx       # Componente para testar conexão com MinIO
│   │   │   └── MinioUpload.jsx     # Componente para upload de arquivos ao MinIO
│   │   ├── styles/
│   │   │   ├── components.css      # Estilos específicos de componentes
│   │   │   └── global.css          # Estilos globais da aplicação
│   │   ├── App.jsx                 # Componente principal da aplicação
│   │   ├── index.css               # Estilo base
│   │   └── index.jsx               # Ponto de entrada do React
│   ├── Dockerfile.dev              # Dockerfile para desenvolvimento do frontend
│   ├── Dockerfile.prod             # Dockerfile para produção do frontend
│   ├── index.html                  # HTML principal do frontend
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml              # Orquestração dos containers
├── .env                            # Variáveis de ambiente
├── .env.example                    # Exemplo de configuração
├── .gitignore
├── run_dev.ps1                     # Script de desenvolvimento para Windows
└── README.md
```

---

## 🧪 Testes

- **Frontend local**

  ```bash
  cd frontend
  npm install
  npm run dev
  ```

- **Backend local (dev)**

  ```bash
  cd backend
  pip install -r requirements-dev.txt
  uvicorn app.main:app --reload
  ```

- **Backend produção**

  ```bash
  cd backend
  pip install -r requirements-prod.txt
  uvicorn app.main:app --host 0.0.0.0 --port 8000
  ```

- **Testes de API** com [Postman](https://www.postman.com/) ou `curl`.

---

## 🛠️ Problemas Comuns

- **Failed to fetch** → Verifique se o backend está rodando e se o CORS está habilitado.
- **MinIO não inicializa** → Confira variáveis `.env` e portas.
- **Banco de dados não conecta** → Certifique-se que o serviço PostgreSQL está ativo.
- **Volumes corrompidos** → Rode:

  ```bash
  docker compose down -v
  docker compose up --build -d
  ```

---

## 🤝 Contribuição

1. Faça um fork
2. Crie uma branch (`git checkout -b feature/minha-feature`)
3. Commit (`git commit -m 'feat: minha feature'`)
4. Push (`git push origin feature/minha-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE).

---

## 📫 Contato

- **Autor:** Davi Soares Dilly
- **E-mail:** [davi.cyebrjatico@gmail.com](mailto:davi.cyebrjatico@gmail.com)
- **GitHub:** [github.com/davisoaresdilly](https://github.com/davisoaresdilly)

---
