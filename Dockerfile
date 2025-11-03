# ✅ Use official Python image with Debian (not Alpine)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# 🔧 Install required system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        libffi-dev \
        python3-dev \
        ffmpeg \
        aria2 \
        build-essential \
    && pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# ✅ Run your bot
CMD ["python", "main.py"]
