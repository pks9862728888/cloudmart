# Use Python 3.13 slim image as base
FROM python:3.13-slim AS base
LABEL version="0.0.1-SNAPSHOT"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN adduser --disabled-password --gecos '' appuser

# Set work directory and change ownership
WORKDIR /app
RUN chown appuser:appuser /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install uv

# Install Python dependencies using uv
COPY --chown=appuser:appuser pyproject.toml uv.lock ./
USER appuser
RUN uv sync --frozen

# Copy application code
COPY --chown=appuser:appuser . .

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health', timeout=5)" || exit 1

# Run the application
CMD ["uv", "run", "main.py"]
