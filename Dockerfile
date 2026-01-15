# Base Image
FROM python:3.9-slim

# Working Directory
WORKDIR /app

# Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Code
COPY . .

# Expose Port
EXPOSE 8000

# Run Application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
