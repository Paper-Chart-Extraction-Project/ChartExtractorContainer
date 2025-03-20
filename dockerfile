# Define directory for ChartExtractor to be installed.
ARG CHARTEXTRACTOR_DIR="/ChartExtractor"

# FROM python:3.12-slim AS build-image
FROM nvidia/cuda:12.3.2-cudnn9-runtime-ubuntu22.04

# Include global arg.
ARG CHARTEXTRACTOR_DIR

# Set noninteractive to avoid tzdata prompts.
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

# Install dependencies and add deadsnakes PPA for Python 3.12
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.12 python3.12-venv python3.12-dev && \
    rm -rf /var/lib/apt/lists/*

# Create a symbolic link for python3.12 to python3, and python3.12 pip to pip3
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1 && \
    python3.12 -m ensurepip && \
    ln -s /usr/bin/pip3.12 /usr/bin/pip3

# Install ChartExtractor
RUN mkdir -p ${CHARTEXTRACTOR_DIR}
COPY README.md pyproject.toml poetry.lock requirements.txt ${CHARTEXTRACTOR_DIR}/
RUN pip3 install poetry
COPY . ${CHARTEXTRACTOR_DIR}/
WORKDIR ${CHARTEXTRACTOR_DIR}
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --without dev
WORKDIR /

# Copy run shell script.
COPY run.sh /tmp/run.sh
COPY run.py /tmp/run.py
RUN chmod +x /tmp/run.sh

ENTRYPOINT /tmp/run.sh
