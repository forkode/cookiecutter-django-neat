# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Start work
1. Clone project from git
2. Run  
     ansible-playbook setup.yml  
   and then you can run:  
     . ./venv/bin/activate  
     ./manage.py runserver_plus  

  Alternatively you can run everything in docker:

        docker-compose up

## Default admin user login and password
TODO Please change the password and remove this section from here!  
user: admin  
password: hitchhikerindulgencesviewpoint  

## Automatic documentation
Automatic documentation is accessible on /admin/doc/

## Preferred codestyle
html/css: https://google.github.io/styleguide/htmlcssguide.html  
python: pep8
