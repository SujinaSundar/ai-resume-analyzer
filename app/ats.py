"""
ATS score calculation module.
"""
from sklearn.metrics.pairwise import cosine_similarity

from app.embeddings import (
    generate_embedding
)

def calculate_ats_score(
    resume_text,
    job_description
):

    resume_embedding = generate_embedding(
        resume_text
    )

    jd_embedding = generate_embedding(
        job_description
    )

    score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return float(round(score * 100, 2))
