FROM python:3.9-slim-buster

WORKDIR /app
ADD . /app

ENV ACCEPT_EULA=Y

COPY requirements.txt requirements.txt

RUN apt-get --assume-yes update

RUN pip3 install -r requirements.txt

COPY . .
