FROM python:3.6

ENV PYTHONBUFFERED 1

RUN mkdir /weddingbook

WORKDIR /weddingbook

ADD . /weddingbook

RUN pip install -r requirements.txt && \ 
    python manage.py makemigrations && \
    python manage.py migrate

EXPOSE 8000