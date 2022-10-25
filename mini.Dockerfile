FROM python:3.9-alpine

COPY requirements/mini-requirements.txt .

RUN pip install --no-cache-dir -r mini-requirements.txt