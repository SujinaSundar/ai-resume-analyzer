# AI Resume Analyzer

AI Resume Analyzer is an intelligent backend application that analyzes resumes, calculates ATS scores, extracts technical skills, and generates interview questions using Large Language Models (LLMs). The project demonstrates modern backend development, DevOps practices, containerization, CI/CD automation, and cloud deployment workflows.

---

# Features

- Resume PDF upload and processing
- ATS score calculation
- Technical skill extraction
- AI-generated interview questions
- REST API using FastAPI
- Docker containerization
- Kubernetes deployment using Helm
- GitHub Actions CI/CD pipeline
- AWS EC2 cloud deployment

---

# Technologies Used

| Category | Technologies |
|---|---|
| Backend Framework | FastAPI |
| Language | Python |
| AI/LLM Integration | Groq API |
| Containerization | Docker |
| Orchestration | Kubernetes |
| Deployment Management | Helm |
| Cloud Platform | AWS EC2 |
| CI/CD | GitHub Actions |
| Package Management | uv |
| Testing | Pytest |
| Code Quality | Pylint |
| Version Control | Git & GitHub |

---

# Project Structure

```bash
ai-resume-analyzer/
│
├── app/
│   ├── main.py
│   ├── ats.py
│   ├── skills.py
│   ├── interview.py
│
├── uploads/
│
├── tests/
│
├── resume-analyzer-chart/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── .gitignore
