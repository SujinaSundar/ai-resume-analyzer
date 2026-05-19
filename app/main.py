import shutil

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Form
)

from app.ats import (
    calculate_ats_score
)

from app.interview import (
    generate_questions
)

from app.parser import (
    extract_text
)

from app.skills import (
    extract_skills
)

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "AI Resume Analyzer Running"
    }

@app.post("/upload-resume")
async def upload_resume(

    file: UploadFile = File(...),

    job_description: str = Form(...)

):

    if not file.filename.endswith(".pdf"):

        return {
            "error": "Only PDF files allowed"
        }

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Extract text
    resume_text = extract_text(
        file_path
    )

    # ATS Score
    score = calculate_ats_score(
        resume_text,
        job_description
    )

    # Extract skills
    skills = extract_skills(
        resume_text
    )

    # Generate AI questions
    questions = generate_questions(
        skills
    )

    return {

        "filename": file.filename,

        "ats_score": score,

        "skills": skills,

        "interview_questions": questions
    }
