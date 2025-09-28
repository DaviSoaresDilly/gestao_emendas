# backend/app/schemas.py

from pydantic import BaseModel

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