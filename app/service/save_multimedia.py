from sqlalchemy.orm import Session
from app.models.multimedia_file import MultimediaFile

"""
    Guardar en base de datos. 
"""
async def insert_audio_metadata(db: Session, file_name: str, s3_url: str):

    audio_entry = MultimediaFile(file_name=file_name, s3_url=s3_url)
    db.add(audio_entry)
    db.commit()
    db.refresh(audio_entry)
    
    return audio_entry