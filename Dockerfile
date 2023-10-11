# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables for Flask (modify as needed)
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"


# Set the working directory to /app
WORKDIR /app
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY app app/


# Expose port 5000 for the Flask web application
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app/main.py"]
