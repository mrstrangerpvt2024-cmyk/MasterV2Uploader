# ✅ Use Debian Bullseye (Stable + Full Apt repo)
FROM python:3.9-bullseye

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# ✅ Install all dependencies cleanly
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        libffi-dev \
        python3-dev \
        ffmpeg \
        aria2 \
        build-essential \
        wget \
        curl \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# ✅ Upgrade pip first (important!)
RUN pip install --upgrade pip setuptools wheel

# ✅ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Run bot
CMD ["python", "main.py"]
