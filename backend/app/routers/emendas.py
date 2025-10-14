# backend/app/routers/emendas.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..database import SessionLocal

router = APIRouter(
    prefix="/emendas",
    tags=["Emendas"]
)

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Emenda)
def create_emenda(emenda: schemas.EmendaCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova emenda no banco de dados.
    """
    # A lógica complexa fica no crud.py, mantendo o endpoint limpo.
    return crud.create_emenda(db=db, emenda=emenda)


@router.get("/", response_model=List[schemas.Emenda])
def read_emendas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retorna uma lista de emendas.
    """
    emendas = crud.get_emendas(db, skip=skip, limit=limit)
    return emendas