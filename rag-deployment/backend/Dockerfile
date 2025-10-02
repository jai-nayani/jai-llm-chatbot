# Dockerfile for deploying FastAPI backend

FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY ../../requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Copy config from root
COPY ../../config.py .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

