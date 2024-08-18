#API docker file
# official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python application file into the container
COPY app.py .

EXPOSE 8080

CMD ["python3", "app.py"]
