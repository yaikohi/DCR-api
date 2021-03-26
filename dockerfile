FROM python3.9-slim-buster

WORKDIR /DCR-API-PY

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["cd /api", "hypercorn", "main:app", "--reload"]
