from fastapi import APIRouter, UploadFile, File
from app.documents.service import upload_document

router = APIRouter(prefix="/documents", tags=["documents"])

@router.post("/upload")
async def upload_deocument(file: UploadFile = File(...)):
    
    file_path = await upload_document(file)

    return{
        "filename": file.filename,
        "content_type": file.content_type,
        "path": str(file_path)
    }   
