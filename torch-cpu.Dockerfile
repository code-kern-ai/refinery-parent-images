FROM kernai/refinery-parent-images:v1.5.0-common

COPY requirements/torch-cpu-requirements.txt .

RUN pip3 install --no-cache-dir -r torch-cpu-requirements.txt