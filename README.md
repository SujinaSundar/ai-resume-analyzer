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
  "filename": "Sujina_Resume_Honeywell.pdf",
  "ats_score": 46.77,
  "skills": [
    "Python",
    "SQL",
    "NumPy",
    "Pandas",
    "Matplotlib",
    "Scikit-learn",
    "Apache Spark",
    "Spark SQL",
    "Spark MLlib",
    "FastAPI",
    "Docker",
    "REST API Development",
    "Git",
    "Jupyter",
    "LLMs",
    "Retrieval-Augmented Generation",
    "LLM Fine-Tuning",
    "LoRA",
    "PEFT",
    "LlamaIndex",
    "SARIMA",
    "Kaggle",
    "Python",
    "SQL"
  ],
  "interview_questions": [
    "1. Implement a function to check if a given string is a palindrome, ignoring case, spaces, and punctuation.",
    "2. Write a Python function to find the first duplicate in an array of integers. If no duplicates are found, return None.",
    "3. Design a Python function to find the maximum sum of a subarray within a given one-dimensional array of integers.",
    "1. Write a SQL query to retrieve the top 3 highest paying jobs from the employees table, along with the average salary of each job.",
    "2. You have two tables, orders and customers. The orders table has columns order_id, customer_id, order_date, and total. The customers table has columns customer_id, name, and email. Write a SQL query to retrieve the total amount spent by each customer, along with their name and email.",
    "3. Given a table with the following structure: id (primary key), name, age, and salary. Write a SQL query to retrieve the names of all employees who are either 30 years old or older, and have a salary greater than the average salary of all employees.",
    "1. Write a function to create a 2D NumPy array with dimensions 3x4 filled with zeros, and then replace the first row with a 1D array [1, 2, 3, 4].",
    "2. Given two 1D NumPy arrays, write a function to find the intersection of two arrays, i.e., the elements that are present in both arrays.",
    "3. Write a function to perform element-wise multiplication of two 2D NumPy arrays, and then calculate the mean of the resulting array along the second axis.",
    "1. Write a Pandas function to efficiently merge two DataFrames with different indexes, assuming that the common column is named 'id'.",
    "2. You have a DataFrame with a column 'date' in string format ('YYYY-MM-DD'). Write a Pandas function to convert this column to datetime format and then calculate the difference between the maximum and minimum dates.",
    "3. You have a DataFrame with a column 'name' and another column 'age'. Write a Pandas function to filter out rows where the age is greater than 50 and then group the remaining rows by 'name' to calculate the average age.",
    "1. Create a Matplotlib plot that displays the distribution of a normal distribution with a mean of 0 and a standard deviation of 1. Include a title, labels, and a legend.",
    "2. Write a function that generates a scatter plot of a dataset with x and y coordinates. The function should take in a pandas DataFrame as input and plot the points with different colors based on a categorical column in the DataFrame.",
    "3. Create a Matplotlib bar chart that displays the top 5 most frequent words in a given text, along with their frequencies. The text is stored in a string and the words are separated by spaces."
  ]
}
```


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

