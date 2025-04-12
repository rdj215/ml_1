FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy files into container

COPY . /app

# Install dependencies
RUN pip install fastapi uvicorn scikit-learn numpy python-multipart 

# Expose port the app runs on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]