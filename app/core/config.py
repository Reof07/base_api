import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

class Settings(BaseSettings):
    # Configuración común
    APP_NAME: str = "Smart files"
    DEBUG: bool = False
    DATABASE_URL: str = ""
    API_KEY_TOKEN: str
    FASTAPI_ENV: str

    # Database variables
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_DATABASE: str
    DB_USERNAME: str = "root"
    DB_PASSWORD: str = ""

    # AWS S3 Credentials
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_DEFAULT_REGION: str
    AWS_BUCKET: str
    AWS_USE_PATH_STYLE_ENDPOINT: bool = False
    
    # OPENAI API
    OPENAI_API_KEY: str
    
    class Config:
        # Para permitir la carga desde archivos .env
        env_file = ".env"
        extra = "ignore"

class DevelopmentSettings(Settings):
    DEBUG: bool = True
    DATABASE_URL: str = (
        f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
    )
    # Imprimir para depuración
    print(f"Development DATABASE_URL: {DATABASE_URL}")

class ProductionSettings(Settings):
    DEBUG: bool = False
    DATABASE_URL: str = (
        f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
    )

# Manejamos el entorno actual (development o production)
def get_settings() -> Settings:
    env = os.getenv("FASTAPI_ENV", "development")  # Si no hay valor en .env, default es 'development'
    print(f"Running environment: {env}")
    if env == "production":
        return ProductionSettings()
    return DevelopmentSettings()

# Obtenemos la configuración actual
settings = get_settings()
