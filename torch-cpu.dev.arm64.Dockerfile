FROM registry.dev.onetask.ai/code-kern-ai/refinery-parent-images:CURRENT_BRANCH_NAME-common-arm64

COPY requirements/torch-cpu-requirements.txt .

RUN pip3 install --no-cache-dir -r torch-cpu-requirements.txt