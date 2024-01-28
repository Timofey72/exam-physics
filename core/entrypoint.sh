#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py loaddata data.json

gunicorn core.wsgi:application --bind 0.0.0.0:8000