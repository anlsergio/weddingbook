FROM python:3.6

ENV PYTHONBUFFERED 1

RUN mkdir /weddingbook

WORKDIR /weddingbook

ADD . /weddingbook

RUN pip install -r requirements.txt

ENTRYPOINT [ "./entrypoint.sh" ]

EXPOSE 8000