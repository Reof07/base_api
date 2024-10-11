import os
import asyncio

from app.core.config import settings
from app.service.save_multimedia import insert_audio_metadata
from app.utils.utils import normalize_filename, save_temp_file, verify_output_file
from app.service.extract_audio import extract_audio
from app.service.upload_to_s3 import upload_to_s3


async def process_audio_file(file, db):
    temp_input_file = f"./app/media/{normalize_filename(file.filename)}"
    output_file = None  # Inicializar como None
    
    try:
        # Guardar archivo temporal
        await save_temp_file(file, temp_input_file)

        # Extraer audio (ejecutar en un hilo si es sincrónica)
        output_file = await asyncio.to_thread(extract_audio, temp_input_file)

        # Verificar si el archivo MP3 realmente existe
        verify_output_file(output_file)

        # Obtener nombre del archivo para S3
        s3_file_name = os.path.basename(output_file)
        s3_url = await upload_to_s3(output_file, settings.AWS_BUCKET, s3_file_name)
        # Guardar metadatos en la base de datos
        await insert_audio_metadata(db, s3_file_name, s3_url)

        return {
            "s3_file_name": s3_file_name,
            "s3_url": s3_url
        }

    finally:
        # Limpiar archivos temporales
        if os.path.exists(temp_input_file):
            os.remove(temp_input_file)
        if output_file and os.path.exists(output_file):
            os.remove(output_file)