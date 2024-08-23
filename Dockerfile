FROM python:3.8-slim

# Install build dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
