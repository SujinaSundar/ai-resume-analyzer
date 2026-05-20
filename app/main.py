import os
import shutil

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

from pypdf import PdfReader

from app.skills import extract_skills
from app.interview import generate_questions
from app.ats import calculate_ats_score

app = FastAPI()


UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


def extract_text_from_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text

    return text


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

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    resume_text = extract_text_from_pdf(
        file_path
    )

    ats_score = calculate_ats_score(

        resume_text,

        job_description
    )

    skills = extract_skills(
        resume_text
    )

    interview_questions = generate_questions(
        skills[:5]
    )

    return {

        "filename": file.filename,

        "ats_score": ats_score,

        "skills": skills,

        "interview_questions": interview_questions
    }
