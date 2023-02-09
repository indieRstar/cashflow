FROM python:3.8.16-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1 

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt