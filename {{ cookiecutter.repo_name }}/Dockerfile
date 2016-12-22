FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
ENV DEPLOYMENT production

COPY ./requirements /requirements
RUN apt-get update &&\
    cat /requirements/production-apt.txt | xargs apt-get install -y --no-install-recommends
RUN pip3 install -r /requirements/production-py.txt

COPY ./configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY . /opt/{{ cookiecutter.repo_name }}/
WORKDIR /opt/{{ cookiecutter.repo_name }}/

RUN python3 ./manage.py compilemessages
RUN python3 ./manage.py collectstatic --no-input
RUN python3 ./manage.py check

VOLUME /opt/{{ cookiecutter.repo_name }}/static/
EXPOSE 8000
CMD ["/usr/bin/supervisord"]
