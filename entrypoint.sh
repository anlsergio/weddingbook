#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn weddingbook.wsgi:application -w 3 -b 0.0.0.0:8000