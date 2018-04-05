FROM ubuntu:17.10

ENV DEBIAN_FRONTEND noninteractive

COPY ./ci /opt/{{ cookiecutter.repo_name }}/ci

RUN apt-get update &&\
    apt-get install -y --no-install-recommends apt-utils &&\
    cat /opt/{{ cookiecutter.repo_name }}/ci/apt-requirements.txt | xargs apt-get install -y --no-install-recommends

RUN locale-gen en_US.UTF-8

ENV LANG='en_US.UTF-8'
ENV LC_ALL='en_US.UTF-8'
ENV LANGUAGE='en_US.UTF-8'

RUN python3.6 -m pip install -r /opt/{{ cookiecutter.repo_name }}/ci/py-requirements.txt

COPY . /opt/{{ cookiecutter.repo_name }}/
WORKDIR /opt/{{ cookiecutter.repo_name }}/

RUN mkdir -p locale
RUN python3.6 ./manage.py compilemessages
RUN python3.6 ./manage.py collectstatic --no-input
RUN python3.6 ./manage.py check

RUN useradd -ms /bin/bash django
USER django

VOLUME /opt/{{ cookiecutter.repo_name }}/static/
EXPOSE 8000
ENTRYPOINT ["/opt/{{ cookiecutter.repo_name }}/docker-entrypoint.sh"]
