{{ cookiecutter.project_name }}
==============================

{{ cookiecutter.description }}

## Start work
1. Clone project from git
2. Run
        ./setup.sh
   it will:
     - create virtualenv as env
     - install development requirements
     - migrate database first time
     - install gitt pre-commit hook
   and then you can run:
     . ./env/bin/activate
     ./manage.py runserver_plus

  Then export DEPLOYMENT='development'

  Alternatively you can run everything in docker:

        docker-compose up

## Automatic documentation
Automatic documentation is accessible on /admin/doc/

## Preferred codestyle
html/css: https://google.github.io/styleguide/htmlcssguide.xml  
python: pep8
