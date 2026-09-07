from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from sqlalchemy import text

app = FastAPI()

@app.get('/')
def root():
    return{
        "message": "AI Document Intelligence & Research Assistant"
    }