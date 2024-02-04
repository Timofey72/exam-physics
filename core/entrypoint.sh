#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py loaddata data.json

gunicorn --config gunicorn_config.py core.wsgi:application