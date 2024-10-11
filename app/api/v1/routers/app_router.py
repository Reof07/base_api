
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.service.files_services import process_audio_file

app_router = APIRouter()


@app_router.post("/extract-audio/", 
    description="Uploads a video file from which the audio will be extracted",
)
async def upload_file_endpoint(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Llamar al servicio que hemos refactorizado
        file_uploaded = await process_audio_file(file, db)
        return {"message": "Archivo subido exitosamente", "file_uploaded": file_uploaded}

    except HTTPException as e:
        raise e  # Lanza nuevamente la excepción para que FastAPI la maneje
    
    except Exception as e:
        # Manejar cualquier otro error inesperado
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")