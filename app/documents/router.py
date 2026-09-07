from fastapi import APIRouter, UploadFile, File, Depends
from app.documents.service import save_document
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.documents.schemas import DocumentResponse
from app.documents.service import get_documents

router = APIRouter(prefix="/documents", tags=["documents"])


# Upload a document _____________________________________________________________________________
@router.post("/upload", response_model=DocumentResponse)
async def upload_document(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    
    document = await save_document(file, db)

    return document



# Get a document ________________________________________________________________________________
@router.get("/", response_model=list[DocumentResponse])
async def list_documents(db: AsyncSession = Depends(get_db)):

    documents = await get_documents(db)

    return documents


