# Use Python 3.10 slim
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app/messaging_app

# Copy requirements from outer folder
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy Django project
COPY messaging_app/ /app/messaging_app/

# Expose port
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]