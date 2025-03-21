#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate
# python manage.py loaddata fixtures/*.json
# python manage.py runserver 0.0.0.0:8000

uwsgi --http 0.0.0.0:8000 --workers 4 --master --enable-threads --module core.wsgi