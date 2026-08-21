from fastapi import FastAPI
from app.api.resume import router as resume_router
app = FastAPI(
    title="AI Career Platform",
    description="An AI-powered platform to help users explore and advance their careers.",
)

app.include_router(resume_router)

@app.get("/")
def root():
    return {"message": "Welcome to the AI Career Platform!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
