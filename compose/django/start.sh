#!/bin/bash
set -e

cd the_eye

python manage.py collectstatic --no-input
python manage.py migrate  --no-input --traceback

if [ "${DJANGO_DEBUG}" = "True" ]; then
  python manage.py runserver 0.0.0.0:8000
else
  gunicorn the_eye.wsgi -b 0.0.0.0:8000
fi;
