FROM python:3.5-alpine

MAINTAINER Daniel Saldivar-Salas <daniel.saldivar.ds@gmail.com>

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt
CMD ["python", "./webapp/app.py"]
