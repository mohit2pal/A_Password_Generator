FROM ubuntu:16.10
RUN apt-get update && apt-get install -y python3 python3-pip

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ["python","server.py"]