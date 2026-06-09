# AI Resume Analyzer

An AI-powered Resume Analyzer that evaluates resumes against job descriptions, calculates ATS (Applicant Tracking System) scores, extracts technical skills, and generates interview questions using Large Language Models (LLMs).

## Features

* Upload PDF resumes
* ATS score calculation
* Technical skill extraction
* AI-generated interview questions
* FastAPI REST API
* Docker containerization
* Kubernetes deployment with Helm
* GitHub Actions CI/CD pipeline
* AWS EC2 deployment

---

## Tech Stack

### Backend

* Python
* FastAPI
* PyPDF
* Groq API

### DevOps & Cloud

* Docker
* Kubernetes
* Helm
* GitHub Actions
* AWS EC2

### Testing & Quality

* Pytest
* Pylint
* uv Package Manager

---

## Project Structure

```text
ai-resume-analyzer/
│
├── app/
│   ├── main.py
│   ├── ats.py
│   ├── skills.py
│   ├── interview.py
│
├── frontend/
│   └── resume-analyzer.html
│
├── tests/
│
├── uploads/
│
├── .github/
│   └── workflows/
│
├── Dockerfile
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## System Architecture

```text
User
 │
 ▼
Frontend (HTML/CSS/JS)
 │
 ▼
FastAPI Backend
 │
 ├── ATS Score Calculation
 ├── Skill Extraction
 └── Interview Question Generation
 │
 ▼
Groq LLM API
 │
 ▼
JSON Response
```

---

## API Endpoint

### Upload Resume

```http
POST /upload-resume
```

#### Form Data

| Field           | Type   |
| --------------- | ------ |
| file            | PDF    |
| job_description | String |

---

## Sample Response

```json
{
  "filename": "resume.pdf",
  "ats_score": 86,
  "skills": [
    "Python",
    "FastAPI",
    "Docker",
    "Kubernetes"
  ],
  "interview_questions": [
    "What is FastAPI?",
    "Explain Docker architecture.",
    "What is Kubernetes?"
  ]
}
```

---

## Running Locally

### Create Virtual Environment

```bash
uv venv
```

### Install Dependencies

```bash
uv sync
```

### Create .env

```env
GROQ_API_KEY=your_api_key
```

### Run Application

```bash
uv run uvicorn app.main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Frontend

Launch the frontend using VS Code Live Server:

```text
frontend/resume-analyzer.html
```

The frontend connects to:

```text
http://localhost:8000/upload-resume
```

and displays:

* ATS Score
* Extracted Skills
* Interview Questions

---

## Docker Deployment

### Build Image

```bash
docker build -t resume-analyser:v1 .
```

### Run Container

```bash
docker run -d -p 8000:8000 --env-file .env resume-analyser:v1
```

---

## Kubernetes Deployment

### Create Helm Chart

```bash
helm create resume-analyzer-chart
```

### Install Application

```bash
helm install resume-analyzer ./resume-analyzer-chart
```

### Upgrade Deployment

```bash
helm upgrade resume-analyzer ./resume-analyzer-chart
```

---

## AWS EC2 Deployment

The application is deployed on an Ubuntu EC2 instance using Docker.

### Deployment Workflow

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
SSH into EC2
   │
   ▼
Git Pull
   │
   ▼
Docker Build
   │
   ▼
Container Restart
```

---

## Version Control Strategy

Git and GitHub were used to manage source code.

### Best Practices

* Feature branch development
* Frequent commits
* Meaningful commit messages
* Pull request workflow
* Environment variables excluded from Git

### Benefits

* Better collaboration
* Easier rollback
* Safer deployments

---

## Testing Approach

### Unit Testing

```bash
uv run pytest
```

### Code Quality

```bash
uv run pylint app
```

### Benefits

* Early bug detection
* Improved maintainability
* Consistent coding standards

---

## CI/CD Pipeline

GitHub Actions automates testing and deployment.

### Continuous Integration

* Dependency installation
* Pylint validation
* Pytest execution

### Continuous Deployment

* Connect to EC2 via SSH
* Pull latest code
* Build Docker image
* Restart container

### Trigger

Deployment runs automatically when code is pushed to the deployment branch.

---

## Security Practices

* API keys stored in `.env`
* `.env` excluded using `.gitignore`
* GitHub Secrets used in CI/CD
* SSH key authentication for EC2

---

## Challenges Faced

* Docker image build issues
* Kubernetes image pull errors
* Helm configuration issues
* GitHub Actions YAML debugging
* Environment variable management
* EC2 deployment troubleshooting

---

## Learning Outcomes

This project helped gain practical experience in:

* FastAPI Development
* REST API Design
* Docker
* Kubernetes
* Helm
* GitHub Actions
* AWS EC2
* CI/CD Pipelines
* DevOps Best Practices

---

## Future Improvements

* User Authentication
* Resume History Storage
* Database Integration
* HTTPS with Nginx
* Prometheus Monitoring
* Grafana Dashboards
* AWS EKS Deployment

