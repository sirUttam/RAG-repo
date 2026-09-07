from app.storage.local import upload_dir, save_file
from fastapi import UploadFile


async def upload_document(file: UploadFile):

    file_path = upload_dir / file.filename

    await save_file(file, file_path)

    return file_path

