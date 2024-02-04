#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py loaddata data.json

gunicorn --workers=4 --reload --max-requests=1000 core.wsgi -b 0.0.0.0:8000