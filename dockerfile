# Use a lightweight Python image
FROM python:3.10.16-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port and run app
EXPOSE 443
CMD ["python", "app/run_uvicorn.py"]