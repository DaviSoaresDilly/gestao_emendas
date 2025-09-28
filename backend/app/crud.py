# backend/app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas

# --- CRUD para Municípios ---

def get_municipality(db: Session, municipality_id: int):
    """Busca um único município pelo ID."""
    return db.query(models.Municipality).filter(models.Municipality.id == municipality_id).first()

def get_municipalities(db: Session, skip: int = 0, limit: int = 100):
    """Busca uma lista de municípios com paginação."""
    return db.query(models.Municipality).offset(skip).limit(limit).all()

def create_municipality(db: Session, municipality: schemas.MunicipalityCreate):
    """Cria um novo município no banco de dados."""
    db_municipality = models.Municipality(
        name=municipality.name,
        uf=municipality.uf,
        ibge_code=municipality.ibge_code
    )
    db.add(db_municipality)
    db.commit()
    db.refresh(db_municipality)
    return db_municipality