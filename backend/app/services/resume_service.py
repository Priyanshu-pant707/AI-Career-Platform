from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile, HTTPException


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


ALLOWED_TYPES = {
    "application/pdf"
}


async def save_resume(file: UploadFile):

    # 1. Validate file type
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    # 2. Generate unique ID
    resume_id = str(uuid4())

    # 3. Create unique filename
    filename = f"{resume_id}.pdf"

    file_path = UPLOAD_DIR / filename

    # 4. Read uploaded file
    content = await file.read()

    # 5. Save file
    with open(file_path, "wb") as buffer:
        buffer.write(content)

    return {
        "resume_id": resume_id,
        "filename": file.filename,
        "file_path": str(file_path)
    }