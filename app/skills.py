KNOWN_SKILLS = [

    "Python",
    "FastAPI",
    "Docker",
    "AWS",
    "SQL",
    "TensorFlow",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "SARIMA",
    "Statistical Modeling",
    "Time Series Forecasting",
    "Git",
    "Kubernetes",
    "React",
    "Flask",
    "Django",
    "Azure",
    "GCP",
    "Linux",
    "CI/CD",
    "GitHub Actions",
    "Jenkins",
    "Power BI",
    "Tableau",
    "Excel"
]


def extract_skills(resume_text):

    found_skills = []

    resume_lower = (
        resume_text.lower()
    )

    for skill in KNOWN_SKILLS:

        if skill.lower() in (
            resume_lower
        ):

            found_skills.append(skill)

    return found_skills
