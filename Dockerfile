# Base image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set workdir
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy copy and install package
COPY dist/my_django_project-0.1.0-py3-none-any.whl /app/
RUN pip install my_django_project-0.1.0-py3-none-any.whl

EXPOSE 8000

# Run Django with cmd 
CMD ["python", "-m", "manage.py", "runserver", "0.0.0.0:8000"]
