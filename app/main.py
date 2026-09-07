from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from sqlalchemy import text
from app.documents.router import router as documents_router

app = FastAPI()

app.include_router(documents_router)

@app.get('/')
def root():
    return{
        "message": "AI Document Intelligence & Research Assistant"
    }