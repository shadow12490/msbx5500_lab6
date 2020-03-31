FROM ubuntu:16.04

MAINTAINER Your Name "youremail@example.com"

RUN apt update -y && \
    apt install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD gunicorn --bind 0.0.0.0:$PORT app:app

