# backend/app/routers/municipalities.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..database import SessionLocal

router = APIRouter(
    prefix="/municipalities", # URL base para todos os endpoints neste arquivo
    tags=["Municipalities"]    # Agrupa os endpoints na documentação
)

# Dependência: cria uma sessão de banco de dados para cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Municipality)
def create_municipality(municipality: schemas.MunicipalityCreate, db: Session = Depends(get_db)):
    # Lógica para criar um município, usando a função do crud.py
    return crud.create_municipality(db=db, municipality=municipality)


@router.get("/", response_model=List[schemas.Municipality])
def read_municipalities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Lógica para listar os municípios
    municipalities = crud.get_municipalities(db, skip=skip, limit=limit)
    return municipalities