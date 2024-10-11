import re
import os

from fastapi import HTTPException

#  Normalizar el nombre de archivo para evitar problemas de caracteres especiales
def normalize_filename(filename: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

# Función para guardar el archivo temporalmente
async def save_temp_file(file, temp_input_file):
    os.makedirs(os.path.dirname(temp_input_file), exist_ok=True)
    with open(temp_input_file, "wb") as f:
        content = await file.read()
        f.write(content)


# Función para verificar la existencia del archivo MP3
def verify_output_file(output_file):
    if not os.path.exists(output_file):
        raise HTTPException(status_code=500, detail="El archivo MP3 no se generó correctamente.")