# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY ./backend-fastapi/ ./app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
# COPY ./backend-fastapi ./app

# Expose port 80 for the application
EXPOSE 8084

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "app.main:app",  "--port", "8084"]