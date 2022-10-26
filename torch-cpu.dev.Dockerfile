FROM registry.dev.onetask.ai/refinery-parent-images:CURRENT_BRANCH_NAME-common

COPY requirements/torch-cpu-requirements.txt .

RUN pip3 install --no-cache-dir -r torch-cpu-requirements.txt