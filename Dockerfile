FROM ubuntu:16.10
RUN apt-get install python3

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ["python","server.py"]