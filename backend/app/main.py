# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from .database import engine
from . import models
from .routers import municipalities, minio # <--- Importe o novo roteador minio

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
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
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


@app.get("/", tags=["Root"])
def read_root():
    """Endpoint principal que confirma que a API está no ar."""
    return {"message": "Bem-vindo à API de Gestão de Emendas"}