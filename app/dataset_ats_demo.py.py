from app.dataset_loader import (
    load_resume_dataset
)

from app.ats import (
    calculate_ats_score
)

df = load_resume_dataset()

resume_text = df.iloc[0]["Resume_str"]

JOB_DESCRIPTION = """
Looking for Python backend engineer
with FastAPI and Docker experience
"""

score = calculate_ats_score(
    resume_text,
    JOB_DESCRIPTION
)

print(score)
