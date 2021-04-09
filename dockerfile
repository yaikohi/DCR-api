# Should you use a venv in a docker image? : https://vsupalov.com/virtualenv-in-docker/ -> yes.
# Should you use a venv in a docker image? : https://stackoverflow.com/questions/48561981/activate-python-virtualenv-in-dockerfile -> no

FROM python:3.9-slim-buster

WORKDIR /app
ADD . /app

ENV ACCEPT_EULA=Y

COPY requirements.txt requirements.txt

RUN apt-get --assume-yes update
RUN pip install -r requirements.txt

COPY . .

CMD ["cd" "api" "hypercorn" "main:app" "--reload"]