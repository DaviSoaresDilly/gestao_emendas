from fastapi import FastAPI, UploadFile, File
from minio import Minio
from minio.error import S3Error
import os
import io
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Config CORS para frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # para testes, pode restringir depois
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Config MinIO
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

# Criar bucket se não existir
if not minio_client.bucket_exists(BUCKET_NAME):
    minio_client.make_bucket(BUCKET_NAME)


@app.get("/")
def root():
    return {"message": "Backend rodando 🚀"}


@app.post("/minio/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Faz upload de arquivo enviado pelo frontend para o bucket MinIO.
    """
    try:
        # Converte bytes do UploadFile em BytesIO (objeto com .read())
        content = await file.read()
        file_data = io.BytesIO(content)

        minio_client.put_object(
            BUCKET_NAME,
            file.filename,
            data=file_data,
            length=len(content),
            content_type=file.content_type
        )
        return {"status": "ok", "filename": file.filename}
    except S3Error as e:
        return {"status": "error", "details": str(e)}
