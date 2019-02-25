FROM python:3.7-alpine

ENV DEBIAN_FRONTEND noninteractive

COPY ./ci /opt/{{ cookiecutter.repo_name }}/ci

RUN apk update &&\
    cat /opt/{{ cookiecutter.repo_name }}/ci/apt-requirements.txt | xargs apk add
RUN python3 -m pip install -r /opt/{{ cookiecutter.repo_name }}/ci/py-requirements.txt

COPY . /opt/{{ cookiecutter.repo_name }}/
WORKDIR /opt/{{ cookiecutter.repo_name }}/
RUN chmod +x /opt/{{ cookiecutter.repo_name }}/docker-entrypoint.sh

VOLUME /opt/{{ cookiecutter.repo_name }}/static/
EXPOSE 8000
ENTRYPOINT ["/opt/{{ cookiecutter.repo_name }}/docker-entrypoint.sh"]

