FROM python:3.9-alpine3.15

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

ENTRYPOINT ["python","server.py"]