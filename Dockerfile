FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
# it tells puython to run in an unbuffered mode which is recommended when running on a docker container . the reason for this is 
# it does not allow python to buffer the output . this avoid some complications

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user

USER user
