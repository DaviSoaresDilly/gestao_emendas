# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from .database import engine
from . import models
from .routers import municipalities, minio, emendas, uploads

# Esta linha é útil para criar as tabelas ao iniciar,
# mas lembre-se que o Alembic é a ferramenta principal para gerenciar o banco.
models.Base.metadata.create_all(bind=engine)

# Configuração de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

app = FastAPI(
    title="API de Gestão de Emendas",
    description="API para gerenciar e planejar emendas parlamentares.",
    version="0.1.0"
)

# Habilitar CORS
origins = ["*"]  # Permitir todas as origens para o desenvolvimento; ajuste conforme necessário para produção
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Inclusão dos Roteadores ---
# Cada conjunto de endpoints relacionados é incluído aqui.
app.include_router(municipalities.router)
app.include_router(minio.router)
app.include_router(emendas.router)
app.include_router(uploads.router)


@app.get("/", tags=["Root"])
def read_root():
    """Endpoint principal que confirma que a API está no ar."""
    return {"message": "Bem-vindo à API de Gestão de Emendas"}