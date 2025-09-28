# backend/app/models.py

from sqlalchemy import (Column, Integer, String, Numeric, ForeignKey, CHAR,
                        TIMESTAMP, Date, Text)
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.sql import func

# Tabela para os Status (ex: "Pago", "Aguardando Empenho", etc.)
# Corresponde à coluna "Status Geral"
class Status(Base):
    __tablename__ = "statuses"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)

# Tabela para os Tipos de Instrumento (ex: "Convênio", "Termo de Fomento")
# Corresponde à coluna "Tipo de Instrumento"
class Instrumento(Base):
    __tablename__ = "instrumentos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)

# Tabela para os Municípios (sem alterações)
class Municipality(Base):
    __tablename__ = "municipalities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    uf = Column(CHAR(2))
    ibge_code = Column(String(20), unique=True)
    emendas = relationship("Emenda", back_populates="municipality")

# Tabela principal de Emendas, agora com todos os campos da planilha
class Emenda(Base):
    __tablename__ = "emendas"

    id = Column(Integer, primary_key=True, index=True)

    # --- CAMPOS DA PLANILHA ---
    ano = Column(Integer, nullable=False, index=True)
    numero_indicacao = Column(String, index=True)
    orgao_sigla = Column(String)
    beneficiario_nome = Column(String)
    beneficiario_cnpj = Column(String(18)) # Formato CNPJ
    data_pagamento = Column(Date)
    agencia_bancaria = Column(String)
    conta_bancaria = Column(String)
    descricao_indicacao = Column(Text)
    valor_indicado = Column(Numeric(14, 2))
    valor_utilizado = Column(Numeric(14, 2))
    valor_pago = Column(Numeric(14, 2))
    instrumento_numero = Column(String)
    instrumento_status = Column(String)
    numero_inciso = Column(String)
    justificativa_retorno = Column(Text)
    justificativa_reprovacao = Column(Text)

    # --- RELACIONAMENTOS (CHAVES ESTRANGEIRAS) ---
    municipality_id = Column(Integer, ForeignKey("municipalities.id"))
    status_id = Column(Integer, ForeignKey("statuses.id"))
    instrumento_id = Column(Integer, ForeignKey("instrumentos.id"))

    municipality = relationship("Municipality", back_populates="emendas")
    status = relationship("Status")
    instrumento = relationship("Instrumento")

    # --- METADADOS ---
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())