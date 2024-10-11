# app/config.py

import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name = 'Smart files'
    admin_email = str
    database_url = str
    secret_key = str
    ENV: str = "development"
    DATABASE_URL: str
    PORT: int = 8000
    DEBUG: bool = False

    class Config:
        env_file = ".env"  # Este se utilizará por defecto

def get_settings() -> Settings:
    env = os.getenv("ENV", "development")
    if env == "production":
        return Settings(_env_file=".env.production")
    return Settings(_env_file=".env.development")

settings = get_settings()
