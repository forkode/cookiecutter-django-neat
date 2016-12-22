#!/bin/sh
python3 -m venv env
. ./env/bin/activate
pip install -r ./requirements/development-py.txt
./manage.py migrate
mkdir -p ./.git/hooks
cp ./configs/pre-commit ./.git/hooks/pre-commit
