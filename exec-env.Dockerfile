FROM python:3.9-slim

RUN apt-get update && \
    apt-get install --no-install-recommends -y curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements/mini-requirements.txt .
COPY requirements/exec-env-requirements.txt .

RUN pip install --no-cache-dir -r exec-env-requirements.txt