# backend/app/routers/uploads.py

import pandas as pd
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import SessionLocal
import logging
from decimal import Decimal, InvalidOperation

router = APIRouter(prefix="/uploads", tags=["Uploads"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/emendas", summary="Faz o upload de uma planilha de emendas e a processa.")
async def upload_emendas_sheet(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="Formato de ficheiro inválido. Por favor, envie um ficheiro .xlsx")

    try:
        df = pd.read_excel(file.file, keep_default_na=False) # Lê tudo como está
        df = df.astype(str).replace('nan', None) # Converte tudo para string e depois 'nan' para None

        column_mapping = {
            'Ano': 'ano', 'Nº Indicação': 'numero_indicacao', 'Órgão - Sigla': 'orgao_sigla',
            'Município': 'municipio_nome', 'Beneficiário': 'beneficiario_nome',
            'Status Geral': 'status_nome', 'Data de Pagamento': 'data_pagamento',
            'Agência Bancária': 'agencia_bancaria', 'Conta Bancária': 'conta_bancaria',
            'Descrição Indicação': 'descricao_indicacao', 'Valor Indicado': 'valor_indicado',
            'Valor Utilizado': 'valor_utilizado', 'Valor Pago': 'valor_pago',
            'Tipo de Instrumento': 'instrumento_nome', 'Nº Instrumento': 'instrumento_numero',
            'Status Instrumento': 'instrumento_status', 'Beneficiário - CNPJ': 'beneficiario_cnpj',
            'Número do Inciso': 'numero_inciso', 'Justif. retorno indicação': 'justificativa_retorno',
            'Justificativa de Reprovação': 'justificativa_reprovacao'
        }
        df.rename(columns=column_mapping, inplace=True)
        
        emendas_criadas = 0
        for index, row in df.iterrows():
            row_dict = row.to_dict()

            if not row_dict.get('municipio_nome'):
                continue
            
            # --- LIMPEZA MANUAL E EXPLÍCITA ---
            # Data de Pagamento: Se não for uma data válida, define como None
            data_str = row_dict.get('data_pagamento')
            try:
                pd.to_datetime(data_str)
            except (ValueError, TypeError):
                row_dict['data_pagamento'] = None

            # Campos Decimais: Converte para Decimal ou define como None
            campos_decimais = ['valor_indicado', 'valor_utilizado', 'valor_pago']
            for campo in campos_decimais:
                valor = row_dict.get(campo)
                try:
                    row_dict[campo] = Decimal(str(valor)) if valor is not None else None
                except (InvalidOperation, ValueError):
                    row_dict[campo] = None
            
            # Lógica do banco...
            municipio = db.query(models.Municipality).filter(models.Municipality.name == row_dict['municipio_nome']).first()
            if not municipio:
                municipio = crud.create_municipality(db, schemas.MunicipalityCreate(name=row_dict['municipio_nome'], uf="--"))

            status = db.query(models.Status).filter(models.Status.nome == row_dict['status_nome']).first()
            if not status:
                status = crud.create_status(db, schemas.StatusCreate(nome=row_dict['status_nome']))

            instrumento = db.query(models.Instrumento).filter(models.Instrumento.nome == row_dict['instrumento_nome']).first()
            if not instrumento:
                instrumento = crud.create_instrumento(db, schemas.InstrumentoCreate(nome=row_dict['instrumento_nome']))
            
            emenda_data = schemas.EmendaCreate(**row_dict, municipality_id=municipio.id, status_id=status.id, instrumento_id=instrumento.id)
            crud.create_emenda(db, emenda_data)
            emendas_criadas += 1

        return {"status": "sucesso", "emendas_importadas": emendas_criadas}

    except Exception as e:
        logging.error(f"Erro CRÍTICO ao processar planilha: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro ao processar o ficheiro: {e}")