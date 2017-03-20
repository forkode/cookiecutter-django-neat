FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
ENV DEPLOYMENT production

RUN locale-gen en_US.UTF-8

ENV LANG='en_US.UTF-8'
ENV LC_ALL='en_US.UTF-8'
ENV LANGUAGE='en_US.UTF-8'

COPY ./requirements /opt/{{ cookiecutter.repo_name }}/requirements
RUN apt-get update &&\
    cat /opt/{{ cookiecutter.repo_name }}/requirements/production-apt.txt | xargs apt-get install -y --no-install-recommends
RUN pip3 install -r /opt/{{ cookiecutter.repo_name }}/requirements/production-py.txt

COPY ./configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY . /opt/{{ cookiecutter.repo_name }}/
WORKDIR /opt/{{ cookiecutter.repo_name }}/

RUN mkdir -p locale

RUN python3 ./manage.py compilemessages
RUN python3 ./manage.py collectstatic --no-input
RUN python3 ./manage.py check

VOLUME /opt/{{ cookiecutter.repo_name }}/static/
EXPOSE 8000
CMD ["/usr/bin/supervisord"]
