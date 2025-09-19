from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from minio import Minio
from minio.error import S3Error
import os
import io
import logging

# ======================
# Configuração de logs
# ======================
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

app = FastAPI()

# ======================
# Habilitar CORS
# ======================
origins = [
    "http://localhost:3000",   # frontend dev
    "http://127.0.0.1:3000",   # alternativa
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.info("🚀 Backend iniciado com CORS habilitado")

# ======================
# Config MinIO
# ======================
MINIO_HOST = os.getenv("MINIO_HOST", "minio")
MINIO_PORT = os.getenv("MINIO_PORT", "9000")
MINIO_USER = os.getenv("MINIO_ROOT_USER", "minioadmin")
MINIO_PASS = os.getenv("MINIO_ROOT_PASSWORD", "minioadmin")

minio_client = Minio(
    f"{MINIO_HOST}:{MINIO_PORT}",
    access_key=MINIO_USER,
    secret_key=MINIO_PASS,
    secure=False
)

BUCKET_NAME = "emendas-bucket"

if not minio_client.bucket_exists(BUCKET_NAME):
    minio_client.make_bucket(BUCKET_NAME)
    logging.info(f"📦 Bucket '{BUCKET_NAME}' criado no MinIO")
else:
    logging.info(f"📦 Bucket '{BUCKET_NAME}' já existe no MinIO")

# ======================
# Rotas
# ======================
@app.get("/")
def root():
    return {"message": "Backend rodando 🚀"}


@app.post("/minio/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Faz upload de arquivo enviado pelo frontend para o bucket MinIO.
    """
    try:
        logging.info(f"⬆️ Recebendo upload: {file.filename}")
        minio_client.put_object(
            BUCKET_NAME,
            file.filename,
            data=file.file,
            length=-1,
            part_size=10 * 1024 * 1024,
            content_type=file.content_type
        )
        logging.info(f"✅ Upload concluído: {file.filename}")
        return {"status": "ok", "filename": file.filename}
    except S3Error as e:
        logging.error(f"❌ Erro no upload: {str(e)}")
        return {"status": "error", "details": str(e)}


@app.get("/minio/test")
def minio_test():
    """
    Cria e lista um arquivo de teste no MinIO.
    """
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
        logging.error(f"❌ Erro no teste: {str(e)}")
        return {"status": "error", "details": str(e)}
