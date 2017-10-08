#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

case "$1" in
    admin)
        export ADMIN_ENABLED=True
        /usr/local/bin/gunicorn {{ cookiecutter.repo_name }}.wsgi -b 0.0.0.0:8000 -w 2
    ;;
    test)
        python3.6 manage.py test
    ;;
    manage)
        python3.6 manage.py "${@:2}"  # pass args from second
    ;;
    *)
        echo starting gunicorn...
        python3.6 manage.py migrate --noinput
        python3.6 manage.py collectstatic --noinput
        /usr/local/bin/gunicorn {{ cookiecutter.repo_name }}.wsgi -b 0.0.0.0:8000 -w 8
    ;;
esac
