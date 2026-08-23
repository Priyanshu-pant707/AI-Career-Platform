import pymupdf
from pathlib import Path


def extract_text_from_pdf(file_path: str) -> str:

    pdf_path = Path(file_path)

    if not pdf_path.exists():
        raise FileNotFoundError("Resume file not found")

    document = pymupdf.open(pdf_path)

    extracted_text = []

    for page in document:
        text = page.get_text()
        extracted_text.append(text)

    document.close()

    return "\n".join(extracted_text)