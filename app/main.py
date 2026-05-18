from fastapi import FastAPI

from app.schemas import (
    AnalysisRequest
)

from app.ats import (
    calculate_ats_score
)
from app.interview import (
    generate_questions
)

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "AI Resume Analyzer Running"
    }

@app.post("/analyze")
def analyze(
    request: AnalysisRequest
):

    score = calculate_ats_score(
        request.resume_text,
        request.job_description
    )

    return {
        "ats_score": score
    }

@app.get("/questions/{skill}")
def questions(skill: str):

    result = generate_questions(skill)

    return {
        "questions": result
    }

def main():
    print("Hello from ai-resume-analyzer!")


if __name__ == "__main__":
    main()
