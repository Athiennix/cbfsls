# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /Scheduler

# Copy requirements.txt to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Specify the command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout=30", "app:app"]