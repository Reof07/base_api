import os
from typing import Annotated
from dotenv import load_dotenv

from fastapi import Header, HTTPException, status


load_dotenv()
API_KEY = os.getenv("API_KEY_TOKEN")

async def get_token_header(X_Token: Annotated[str, Header()]):
    if X_Token != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-Token header invalid")
