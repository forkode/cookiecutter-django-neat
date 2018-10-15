from fabric.api import local


def setup():
    local('cp .env.example .env')
    local('docker-compose build')


def update():
    local('docker-compose down')
    local('docker-compose build')


def up():
    local('docker-compose up -d')


def run(command):
    local(f'docker-compose run {{ cookiecutter.repo_name }} {command}')


def bash():
    run('bash')


def manage(command):
    run(f'/usr/bin/python3 /opt/{{ cookiecutter.repo_name }}/manage.py {command}')


def migrate():
    manage('migrate')


def runserver():
    local(
        'docker-compose run -p 8000:8000 {{ cookiecutter.repo_name }} '
        '/usr/bin/python3 /opt/{{ cookiecutter.repo_name }}/manage.py '
        'runserver 0.0.0.0:8000'
    )


def makemigrations(args=''):
    manage(f'makemigrations {args}')


def createsuperuser():
    manage('createsuperuser')


def shell():
    manage('shell')
