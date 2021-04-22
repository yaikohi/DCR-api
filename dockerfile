# Should you use a venv in a docker image? : https://vsupalov.com/virtualenv-in-docker/ -> yes.
# Should you use a venv in a docker image? : https://stackoverflow.com/questions/48561981/activate-python-virtualenv-in-dockerfile -> no

# hypercorn/fastapi image: https://github.com/bynect/hypercorn-fastapi-docker

FROM bynect/hypercorn-fastapi:python3.9-slim

ENV ACCEPT_EULA=Y

COPY . .
WORKDIR /

RUN apt-get --assume-yes update
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt