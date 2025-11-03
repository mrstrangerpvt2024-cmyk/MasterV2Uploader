# 🐍 Use a more compatible base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# 🧩 Install system dependencies
RUN apt update && apt install -y \
    gcc \
    g++ \
    libffi-dev \
    python3-dev \
    ffmpeg \
    aria2 \
    && pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt \
    && apt clean && rm -rf /var/lib/apt/lists/*

# 🚀 Run the bot
CMD ["python", "main.py"]
