
from fastapi import FastAPI
from .config import settings

app = FastAPI()

@app.get("/info")
def read_root():
    return {"message": f"Hello, World! Running in {settings.ENV} mode."}

