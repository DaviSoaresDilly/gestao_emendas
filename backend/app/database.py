# backend/app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Pega as variáveis de ambiente para a conexão com o banco
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "gestao_emendas")

# Monta a URL de conexão
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Cria o "motor" de conexão com o banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria uma sessão para cada requisição
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos (tabelas) do SQLAlchemy
Base = declarative_base()