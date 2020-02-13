FROM python:3.6

ENV PYTHONBUFFERED 1

EXPOSE 8081

RUN mkdir /weddingbook

WORKDIR /weddingbook

ADD . /weddingbook

RUN pip install --no-cache-dir -r requirements.txt\
    && find . -type f -name "*.pyc" -delete || true

ENTRYPOINT [ "./entrypoint.sh" ]