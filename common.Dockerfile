FROM python:3.9-slim

COPY requirements/mini-requirements.txt .
COPY requirements/common-requirements.txt .

RUN pip install --no-cache-dir -r common-requirements.txt