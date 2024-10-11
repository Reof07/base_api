from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime
from app.db.database import Base

class MultimediaFile(Base):
    
    __tablename__ = 'multimedia_files'

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(255), nullable=False)  
    s3_url = Column(String(2048), nullable=False) 
    created_at = Column(DateTime, default=func.now())


# Crear tablas en la base de datos
def init_db(engine):
    Base.metadata.create_all(bind=engine)