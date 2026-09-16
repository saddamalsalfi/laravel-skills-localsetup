# Multi-registry compatible production container
FROM python:3.11-slim-bookworm

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first for efficient layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy repository assets
COPY . .

# Create and switch to non-privileged security user
RUN useradd -m -u 10001 mcpuser && chown -R mcpuser:mcpuser /app
USER mcpuser

# Expose standard I/O communication channel
ENTRYPOINT ["python", "server.py"]
