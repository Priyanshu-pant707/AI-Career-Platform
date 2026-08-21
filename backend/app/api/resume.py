from fastapi import APIRouter, UploadFile, File

from app.services.resume_service import save_resume


router = APIRouter(
    prefix="/api/resume",
    tags=["Resume"]
)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    result = await save_resume(file)

    return {
        "message": "Resume uploaded successfully",
        **result
    }