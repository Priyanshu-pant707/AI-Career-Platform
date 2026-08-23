from app.services.resume_ingestion import extract_text_from_pdf


file_path = "uploads/f81398f6-2132-4608-a8cb-561672cd4e99.pdf"

text = extract_text_from_pdf(file_path)

print(text)