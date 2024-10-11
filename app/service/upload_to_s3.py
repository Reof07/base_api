import boto3

from fastapi import HTTPException

from app.core.config import settings


# Configurar el cliente de S3 con credenciales explícitas
s3 = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_DEFAULT_REGION
)

"""
    Función para subir un archivo a S3
"""
async def upload_to_s3(file_path: str, bucket_name: str, s3_file_name: str) -> str:
    try:

        s3_file_name = f"mp3_files/{s3_file_name}"
        s3.upload_file(file_path, bucket_name, s3_file_name)
        s3_url = f"https://{bucket_name}.s3.{settings.AWS_DEFAULT_REGION}.amazonaws.com/{s3_file_name}"
        return s3_url
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al subir archivo a S3: {str(e)}")