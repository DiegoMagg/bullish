FROM python:3.11-slim

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1
ENV TZ="America/Sao_Paulo"

WORKDIR /app

RUN apt update && apt install --no-install-recommends -y && \
  pip3 install --no-cache-dir --upgrade pipenv pip && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

ADD /app /app

RUN pipenv install && \
  pipenv run python manage.py collectstatic --no-input && \
  rm -rf /root/.cache/*
