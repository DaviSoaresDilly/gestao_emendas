# backend/app/schemas.py

from pydantic import BaseModel
from datetime import date
from decimal import Decimal

# Schema para a criação de um município (o que o usuário envia)
class MunicipalityCreate(BaseModel):
    name: str
    uf: str
    ibge_code: str | None = None

# Schema para a leitura de um município (o que a API retorna)
# Inclui o 'id' que é gerado pelo banco e herda os outros campos.
class Municipality(MunicipalityCreate):
    id: int

    class Config:
        orm_mode = True # Ajuda o Pydantic a converter o objeto do banco para este schema

# --- Schemas para Status ---
class StatusBase(BaseModel):
    nome: str

class StatusCreate(StatusBase):
    pass

class Status(StatusBase):
    id: int

    class Config:
        orm_mode = True

# --- Schemas para Instrumento ---
class InstrumentoBase(BaseModel):
    nome: str

class InstrumentoCreate(InstrumentoBase):
    pass

class Instrumento(InstrumentoBase):
    id: int

    class Config:
        orm_mode = True

# --- Schemas para Emenda ---

# Schema base com todos os campos que uma emenda pode ter
class EmendaBase(BaseModel):
    ano: int
    numero_indicacao: str | None = None
    valor_indicado: Decimal
    municipality_id: int
    status_id: int
    instrumento_id: int
    # Adicione outros campos da sua planilha que serão enviados via API
    # Exemplo:
    beneficiario_nome: str | None = None
    descricao_indicacao: str | None = None
    valor_pago: Decimal | None = None
    data_pagamento: date | None = None


# Schema para a criação de uma emenda (o que o frontend envia)
class EmendaCreate(EmendaBase):
    pass


# Schema para a leitura de uma emenda (o que a API retorna)
# Inclui o 'id' e os dados completos dos relacionamentos
class Emenda(EmendaBase):
    id: int
    municipality: Municipality # Mostra os dados completos do município
    status: Status             # Mostra os dados completos do status
    instrumento: Instrumento     # Mostra os dados completos do instrumento

    class Config:
        orm_mode = True # Essencial para converter dados do SQLAlchemy para Pydantic