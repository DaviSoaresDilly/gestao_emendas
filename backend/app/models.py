# backend/app/models.py

from sqlalchemy import (Column, Integer, String, Numeric, ForeignKey, CHAR,
                        TIMESTAMP, Date, Text)
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.sql import func

class Status(Base):
    __tablename__ = "statuses"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    
    # CORREÇÃO: Adiciona a relação inversa, informando que um Status pode ter várias emendas.
    emendas = relationship("Emenda", back_populates="status")

class Instrumento(Base):
    __tablename__ = "instrumentos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)

    # CORREÇÃO: Adiciona a relação inversa.
    emendas = relationship("Emenda", back_populates="instrumento")

class Municipality(Base):
    __tablename__ = "municipalities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    uf = Column(CHAR(2))
    ibge_code = Column(String(20), unique=True)
    emendas = relationship("Emenda", back_populates="municipality")

class Emenda(Base):
    __tablename__ = "emendas"
    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False, index=True)
    numero_indicacao = Column(String, index=True)
    orgao_sigla = Column(String)
    beneficiario_nome = Column(String)
    beneficiario_cnpj = Column(String(18))
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
    municipality_id = Column(Integer, ForeignKey("municipalities.id"))
    status_id = Column(Integer, ForeignKey("statuses.id"))
    instrumento_id = Column(Integer, ForeignKey("instrumentos.id"))
    municipality = relationship("Municipality", back_populates="emendas")
    
    # CORREÇÃO: Completa a relação bidirecional com Status e Instrumento.
    status = relationship("Status", back_populates="emendas")
    instrumento = relationship("Instrumento", back_populates="emendas")

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())