FROM python:3.6.1-alpine

ADD . /a_password_generator

WORKDIR /a_password_generator

RUN pip install -r requirements.txt

CMD ["python", "app.py"]