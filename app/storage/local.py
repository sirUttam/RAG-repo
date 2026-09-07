from pathlib import Path
from fastapi import UploadFile

upload_dir = Path("uploads/documents")
upload_dir.mkdir(parents=True, exist_ok=True)

async def save_file(file: UploadFile, path: Path):

    content = await file.read()
    path.write_bytes(content)