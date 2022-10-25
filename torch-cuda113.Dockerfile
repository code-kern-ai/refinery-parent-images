FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

COPY requirements/mini-requirements.txt .
COPY requirements/common-requirements.txt .
COPY requirements/torch-cuda113-requirements.txt .

RUN pip install --no-cache-dir -r torch-cuda113-requirements.txt 