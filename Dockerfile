FROM continuumio/anaconda3:2020.11

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

ENTRYPOINT [ "python","server.py" ]
