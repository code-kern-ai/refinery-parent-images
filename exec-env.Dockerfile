FROM python:3.10-slim

COPY requirements/mini-requirements.txt .
COPY requirements/exec-env-requirements.txt .

RUN pip install --no-cache-dir -r exec-env-requirements.txt