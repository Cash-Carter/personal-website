FROM python:3.10.16-slim AS base

WORKDIR /app

COPY requirements.txt .
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

COPY . .

FROM base AS dev
EXPOSE 8000
CMD ["python", "app/run_uvicorn.py", "--reload", "--dev"]

FROM base AS prod
EXPOSE 443
CMD ["python", "app/run_uvicorn.py"]