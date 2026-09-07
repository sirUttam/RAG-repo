from app.storage.local import upload_dir, save_file
from fastapi import UploadFile
from app.db.models.document import Document
from sqlalchemy import select


# Save a document to the database and the storage ________________________________________________
async def save_document(file: UploadFile, db):

    file_path = upload_dir / file.filename

    await save_file(file, file_path)

    document = Document(
        filename = file.filename,
        content_type = file.content_type,
    )

    db.add(document)

    await db.commit()

    await db.refresh(document)

    return document



# Get a document from the database ________________________________________________________________
async def get_documents(db):
    result = await db.execute(select(Document))

    return result.scalars().all()


# Get a document by id ________________________________________________________________________________
async def get_document_by_id(document_id: int, db):

    result = await db.execute(select(Document).where(Document.id == document_id))

    return result.scalar_one_or_none()

    