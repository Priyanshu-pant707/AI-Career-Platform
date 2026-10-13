
from pathlib import Path
from uuid import UUID

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.resume_service import save_resume
from app.services.resume_ingestion import extract_text_from_pdf
from app.services.resume_parser import parse_resume_text
from app.schemas.resume import ResumeSchema


router = APIRouter(
    prefix="/api/resume",
    tags=["Resume"]
)


# 1. Existing API: Upload resume
@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):
    result = await save_resume(file)

    return {
        "message": "Resume uploaded successfully",
        **result
    }


# 2. New API: Analyze uploaded resume
@router.post("/{resume_id}/analyze", response_model=ResumeSchema)
def analyze_resume(resume_id: UUID):
    backend_dir = Path(__file__).resolve().parents[2]
    file_path = backend_dir / "uploads" / f"{resume_id}.pdf"

    if not file_path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Resume not found. Upload the PDF first."
        )

    try:
        # Extract text from the PDF
        text = extract_text_from_pdf(str(file_path))

        if not text.strip():
            raise HTTPException(
                status_code=422,
                detail="No extractable text found in this PDF."
            )

        # Extract structured information using the LLM
        resume = parse_resume_text(text)

        return resume

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Resume analysis failed. Check the parser and LLM configuration."
        )
