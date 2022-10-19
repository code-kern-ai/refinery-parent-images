FROM kernai/refinery-parent-images:v0.0.1-common

COPY requirements/torch-cpu-requirements.txt .

RUN pip3 install --no-cache-dir -r torch-cpu-requirements.txt