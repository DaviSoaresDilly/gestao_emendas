# backend/app/routers/minio.py

import os
import logging
import io
from fastapi import APIRouter, UploadFile, File, HTTPException
from minio import Minio
from minio.error import S3Error

router = APIRouter(
    prefix="/minio",
    tags=["MinIO"]
)

# --- Configuração do Cliente MinIO ---
# (Essa lógica agora vive aqui, junto com as rotas que a utilizam)
MINIO_HOST = os.getenv("MINIO_HOST", "minio")
MINIO_PORT = os.getenv("MINIO_PORT", "9000")
MINIO_USER = os.getenv("MINIO_ROOT_USER", "minioadmin")
MINIO_PASS = os.getenv("MINIO_ROOT_PASSWORD", "minioadmin")

try:
    minio_client = Minio(
        f"{MINIO_HOST}:{MINIO_PORT}",
        access_key=MINIO_USER,
        secret_key=MINIO_PASS,
        secure=False
    )
    BUCKET_NAME = "emendas-bucket"
    # Garante que o bucket exista ao iniciar
    if not minio_client.bucket_exists(BUCKET_NAME):
        minio_client.make_bucket(BUCKET_NAME)
        logging.info(f"📦 Bucket '{BUCKET_NAME}' criado no MinIO")
    else:
        logging.info(f"📦 Bucket '{BUCKET_NAME}' já existe no MinIO")
except Exception as e:
    logging.error(f"❌ Não foi possível conectar ao MinIO: {e}")
    minio_client = None


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Faz upload de arquivo para o bucket MinIO."""
    if not minio_client:
        raise HTTPException(status_code=503, detail="Serviço MinIO indisponível.")
    try:
        logging.info(f"⬆️ Recebendo upload: {file.filename}")
        minio_client.put_object(
            BUCKET_NAME,
            file.filename,
            data=file.file,
            length=-1, # O FastAPI/Uvicorn cuida do tamanho
            part_size=10 * 1024 * 1024,
            content_type=file.content_type
        )
        logging.info(f"✅ Upload concluído: {file.filename}")
        return {"status": "ok", "filename": file.filename}
    except S3Error as e:
        logging.error(f"❌ Erro no upload do MinIO: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro no S3: {e}")


@router.get("/test")
def minio_test():
    """Cria e lista um arquivo de teste no MinIO."""
    if not minio_client:
        raise HTTPException(status_code=503, detail="Serviço MinIO indisponível.")
    try:
        test_file = "hello.txt"
        content = "Teste de upload no MinIO com FastAPI 🚀".encode("utf-8")
        file_data = io.BytesIO(content)
        minio_client.put_object(
            BUCKET_NAME,
            test_file,
            data=file_data,
            length=len(content),
            content_type="text/plain"
        )
        objects = [obj.object_name for obj in minio_client.list_objects(BUCKET_NAME)]
        logging.info(f"🔍 Objetos no bucket: {objects}")
        return {"status": "ok", "bucket": BUCKET_NAME, "objects": objects}
    except S3Error as e:
        logging.error(f"❌ Erro no teste do MinIO: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro no S3: {e}")