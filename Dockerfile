# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.158.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
FROM python:3.8.5-alpine

ENV PYTHONUNBUFFERED 1

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

RUN mkdir /workspace
WORKDIR /workspace/restapi
COPY ./ /workspace

# RUN adduser -D user
USER root