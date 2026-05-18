FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install uv

RUN uv sync

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]