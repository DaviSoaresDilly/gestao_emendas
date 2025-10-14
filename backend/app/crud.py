# backend/app/crud.py

from sqlalchemy.orm import Session, joinedload
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

# --- CRUD para Emendas ---

def get_emendas(db: Session, skip: int = 0, limit: int = 100):
    """
    Busca uma lista de emendas com seus relacionamentos (município, status, instrumento).
    O `joinedload` otimiza a consulta, trazendo tudo de uma vez.
    """
    return (
        db.query(models.Emenda)
        .options(
            joinedload(models.Emenda.municipality),
            joinedload(models.Emenda.status),
            joinedload(models.Emenda.instrumento),
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_emenda(db: Session, emenda: schemas.EmendaCreate):
    """Cria uma nova emenda no banco de dados."""
    # Converte o schema Pydantic para um dicionário e cria o objeto do SQLAlchemy
    db_emenda = models.Emenda(**emenda.dict())
    
    db.add(db_emenda)
    db.commit()
    db.refresh(db_emenda)
    return db_emenda

# --- CRUD para Status ---
def create_status(db: Session, status: schemas.StatusCreate):
    db_status = models.Status(**status.dict())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

# --- CRUD para Instrumento ---
def create_instrumento(db: Session, instrumento: schemas.InstrumentoCreate):
    db_instrumento = models.Instrumento(**instrumento.dict())
    db.add(db_instrumento)
    db.commit()
    db.refresh(db_instrumento)
    return db_instrumento