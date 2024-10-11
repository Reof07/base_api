import logging

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.database import engine
from app.api.v1.routers.app_router import app_router 
from app.dependencies import get_token_header
from app.models.multimedia_file import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Smart Files",
    description="Service that extracts audio from MP4 videos and generates summaries of PDF documents, optimizing multimedia and text file processing.",
    version="0.0.1",
    debug=settings.DEBUG
)

# Configuración de CORS: restringir a los orígenes permitidos en producción
origins = [
    "http://127.0.0.1:8000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Solo permitir los dominios especificados
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Restringir métodos permitidos
    allow_headers=["Authorization", "Content-Type"],  # Restringir headers permitidos
)

# Inicializar la base de datos
init_db(engine)

# app router
app.include_router(
    app_router,
    prefix="/api",
    tags=["smart_files"],
    dependencies=[Depends(get_token_header)]
)

# Endpoint de verificación de estado (Health Check)
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Endpoint de información general
@app.get("/info")
def read_root():
    return {
        "message": f" Hello, World! the app: {settings.APP_NAME} is Running in {settings.FASTAPI_ENV} mode."}
