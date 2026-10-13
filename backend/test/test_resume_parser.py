
# from app.services.resume_parser import parse_resume_text


# sample_text = """
# Priyanshu Pant
# Email: priyanshu@example.com
# Phone: 9876543210
# Skills: Python, C++, FastAPI
# """

# resume = parse_resume_text(sample_text)

# print(resume.model_dump())





from app.services.resume_ingestion import extract_text_from_pdf
from app.services.resume_parser import parse_resume_text


file_path = (
    "uploads/f81398f6-2132-4608-a8cb-561672cd4e99.pdf"
)

# Step 1: Extract text using PyMuPDF
text = extract_text_from_pdf(file_path)

# Step 2: Analyze resume using Groq
resume = parse_resume_text(text)

# Step 3: Display structured output
print(resume.model_dump_json(indent=2))
