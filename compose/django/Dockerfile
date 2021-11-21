FROM python:3.9.7-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./the_eye/requirements.txt .
RUN pip install -r requirements.txt

COPY . .
