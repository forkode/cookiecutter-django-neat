FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

COPY ./requirements /requirements
RUN apt-get update &&\
    cat /requirements/production-apt.txt | xargs apt-get install -y --no-install-recommends
RUN pip install -r /requirements/production-py.txt

COPY ./configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY . /opt/{{ cookiecutter.repo_name }}/
WORKDIR /opt/{{ cookiecutter.repo_name }}/

RUN ./manage.py compilemessages
RUN ./manage.py collectstatic --no-input

VOLUME /opt/{{ cookiecutter.repo_name }}/static/
EXPOSE 8000
CMD ["/usr/bin/supervisord"]
