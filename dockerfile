# syntax=docker/dockerfile:1

# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set environment variables to prevent Python from buffering output and writing pyc files
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create a non-privileged user for security
RUN useradd --create-home --shell /bin/bash app_user && \
    chown -R app_user:app_user /app

# Switch to the non-privileged user
USER app_user

# Set the entrypoint to run the CLI tool
ENTRYPOINT ["python", "main.py"]

# Default command to show help if no arguments are provided
CMD ["--help"]