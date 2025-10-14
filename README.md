# Gestão de Emendas Parlamentares 🚀

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-green)]()
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-black?logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18-blue?logo=react)](https://react.dev/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue?logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-blue?logo=docker)](https://www.docker.com/)

Sistema fullstack para gestão e planejamento de emendas parlamentares, construído com uma arquitetura moderna e escalável, focado na importação de dados via planilhas.

---

## 📑 Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [✨ Funcionalidades](#-funcionalidades)
- [🛠️ Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [🏛️ Arquitetura](#️-arquitetura)
- [⚡ Pré-requisitos](#-pré-requisitos)
- [🔧 Configuração e Instalação](#-configuração-e-instalação)
- [🏃 Como Rodar](#-como-rodar)
- [📂 Estrutura do Projeto](#-estrutura-do-projeto)
- [🔗 Endpoints da API](#-endpoints-da-api)
- [🧪 Testes](#-testes)
- [🤔 Problemas Comuns](#-problemas-comuns)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)

---

## 📝 Sobre o Projeto

O **Gestão de Emendas** é um sistema projetado para centralizar, organizar e otimizar o fluxo de trabalho relacionado a emendas parlamentares. A plataforma visa fornecer uma base moderna, escalável e segura para o cadastro, acompanhamento de status e gestão de beneficiários, com um foco principal na importação de dados a partir de planilhas `.xlsx`.

O objetivo é transformar a gestão, que muitas vezes é feita em planilhas descentralizadas, em um processo de dados estruturado, rastreável e inteligente.

---

## ✨ Funcionalidades

-   ✅ **Importação de Planilhas:** Endpoint robusto para upload e processamento de planilhas `.xlsx`, populando o banco de dados de forma automática.
-   ✅ **API RESTful Completa:** Backend com endpoints para CRUD (Create, Read, Update, Delete) de emendas e municípios.
-   ✅ **Criação Automática de Entidades:** O sistema cria automaticamente municípios, status e instrumentos caso não existam durante a importação.
-   ✅ **Visualização de Dados:** Interface em React para listar os dados importados em tempo real.
-   ✅ **Ambiente Containerizado:** Aplicação 100% containerizada com Docker para fácil configuração e portabilidade.
-   ✅ **Desenvolvimento Otimizado:** Ambiente de desenvolvimento com hot-reload para backend e frontend, garantindo máxima produtividade.

---

## 🛠️ Tecnologias Utilizadas

| Categoria     | Tecnologia                                                                                             |
| :------------ | :----------------------------------------------------------------------------------------------------- |
| **Backend** | [Python 3.12](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), [Pydantic](https://pydantic-docs.helpmanual.io/), [Pandas](https://pandas.pydata.org/) |
| **Frontend** | [React 18](https://react.dev/), [Vite](https://vitejs.dev/)                                             |
| **Banco de Dados** | [PostgreSQL 14](https://www.postgresql.org/)                                                         |
| **Armazenamento** | [MinIO](https://min.io/) (Object Storage compatível com S3)                                          |
| **DevOps** | [Docker](https://www.docker.com/), [Docker Compose](https://docs.docker.com/compose/)                       |

---

## 🏛️ Arquitetura

A aplicação segue uma arquitetura de microsserviços containerizados, onde o Frontend (React SPA) se comunica com o Backend (API RESTful em FastAPI) de forma independente. O Backend gerencia a lógica de negócios, o processamento de planilhas e a persistência de dados no PostgreSQL.

```
[Cliente (Navegador)] <--> [Frontend (React Container)] <--> [Backend (FastAPI Container)] <--> [Banco de Dados (PostgreSQL Container)]
```

---

## ⚡ Pré-requisitos

-   [Docker](https://www.docker.com/)
-   [Docker Compose](https://docs.docker.com/compose/)
-   Um navegador moderno (Chrome, Firefox, Edge)

---

## 🔧 Configuração e Instalação

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd gestao_emendas
    ```

2.  **Crie o arquivo de ambiente:**
    Copie o arquivo `.env.example` para um novo arquivo chamado `.env`. As credenciais padrão funcionarão para o ambiente de desenvolvimento.
    ```bash
    cp .env.example .env
    ```

---

## 🏃 Como Rodar

Com o Docker em execução, suba todos os contêineres utilizando o script para PowerShell:

```powershell
./run_dev.ps1
```

Este comando irá construir as imagens (se necessário) e iniciar todos os serviços em modo de desenvolvimento com hot-reload.

Após a inicialização, os serviços estarão disponíveis nos seguintes endereços:

-   🌐 **Frontend:** [http://localhost:3000](http://localhost:3000) (ou a porta que configurou)
-   ⚙️ **Backend (API):** [http://localhost:8000](http://localhost:8000)
-   📚 **Documentação da API (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
-   🗃️ **MinIO Web UI:** [http://localhost:9001](http://localhost:9001)
-   🐘 **PostgreSQL:** Porta `5432`

---

## 📂 Estrutura do Projeto

O projeto é organizado com uma arquitetura limpa e escalável.

```
gestao_emendas/
├── backend/
│   └── app/
│       ├── routers/        # Módulos de rotas da API (endpoints)
│       ├── crud.py         # Funções de interação com o banco (CRUD)
│       ├── database.py     # Configuração da conexão com o banco
│       ├── main.py         # Ponto de entrada da aplicação FastAPI
│       ├── models.py       # Modelos de tabelas do SQLAlchemy
│       └── schemas.py      # Esquemas de validação de dados do Pydantic
├── frontend/
│   └── src/
│       ├── api/            # Funções para chamadas à API
│       ├── components/     # Componentes React reutilizáveis
│       └── styles/         # Ficheiros de CSS
├── .env                    # (Local) Credenciais e variáveis de ambiente
├── .env.example
├── docker-compose.yml      # Orquestração dos containers de produção
├── docker-compose.override.yml # Configurações para o ambiente de desenvolvimento
├── run_dev.ps1             # Script de inicialização para Windows
└── README.md
```

---

## 🔗 Endpoints da API

A API é autogerada e pode ser explorada interativamente em **[http://localhost:8000/docs](http://localhost:8000/docs)**. Os principais endpoints são:

#### `POST /uploads/emendas`
-   **Descrição:** Faz o upload de uma planilha `.xlsx` e importa os dados para o banco.
-   **Corpo:** `multipart/form-data` com um campo `file`.

#### `GET /emendas/`
-   **Descrição:** Lista as emendas cadastradas.

#### `POST /municipalities/`
-   **Descrição:** Cria um novo município.

#### `GET /municipalities/`
-   **Descrição:** Lista os municípios cadastrados.

---

## 🧪 Testes

-   **Testes de API:** Utilize a documentação interativa ([/docs](http://localhost:8000/docs)) para testar os endpoints do backend.
-   **Teste de Frontend:** Acesse a aplicação no navegador e utilize a interface para importar uma planilha e visualizar os resultados.

---

## 🤔 Problemas Comuns

-   **`Failed to fetch` no frontend:** Verifique os logs do contêiner `backend` (`docker compose logs -f backend`). Geralmente é um erro de CORS (resolvido com `origins = ["*"]` no `main.py` para dev) ou um crash no servidor.
-   **`port is already allocated`:** Uma porta que o Docker precisa (ex: 3000, 8000) já está em uso. Pare todos os contêineres (`docker compose down`) e, se persistir, encontre e pare o processo manualmente.
-   **Dados não atualizam:** Se fez alterações no código e elas não refletem, force uma reconstrução completa:
    ```bash
    docker compose down
    docker image rm gestao_emendas-backend
    ./run_dev.ps1
    ```

---

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1.  Faça um **fork** do projeto.
2.  Crie uma nova branch (`git checkout -b feature/minha-feature`).
3.  Faça o commit de suas alterações (`git commit -m 'feat: Adiciona nova feature'`).
4.  Faça o push para a branch (`git push origin feature/minha-feature`).
5.  Abra um **Pull Request**.

---

## 📄 Licença

Este projeto está sob a licença **MIT**.