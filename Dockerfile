# ---------- Stage 1: Builder ----------
    FROM python:3.11-slim AS builder

    WORKDIR /app
    
    RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        && rm -rf /var/lib/apt/lists/*
    
    # Create virtual environment
    RUN python -m venv /opt/venv
    ENV PATH="/opt/venv/bin:$PATH"
    
    COPY requirements.txt .
    RUN pip install --upgrade pip && pip install -r requirements.txt
    
    
    # ---------- Stage 2: Production ----------
    FROM python:3.11-slim AS production
    
    # Create non-root user FIRST
    RUN groupadd --gid 1000 appgroup && \
        useradd --uid 1000 --gid appgroup --shell /bin/bash --create-home appuser
    
    WORKDIR /app
    
    # Runtime dependencies only
    RUN apt-get update && apt-get install -y --no-install-recommends \
        libpq5 \
        && rm -rf /var/lib/apt/lists/* \
        && apt-get clean
    
    # Copy virtualenv from builder
    COPY --from=builder /opt/venv /opt/venv
    ENV PATH="/opt/venv/bin:$PATH"
    
    # Copy application code
    COPY --chown=appuser:appgroup . .
    
    # Create directories for static/media
    RUN mkdir -p staticfiles media && \
        chown -R appuser:appgroup staticfiles media
    
    # Switch to non-root user
    USER appuser
    
    # Collect static files
    RUN python manage.py collectstatic --noinput
    
    EXPOSE 8000
    
    CMD ["gunicorn", "--config", "gunicorn.conf.py", "blog_project.wsgi:application"]

    