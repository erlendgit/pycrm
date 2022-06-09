FROM python:3.10.4-slim

RUN apt update
RUN apt upgrade -y
RUN apt install gettext -y

RUN echo  "alias ls='ls --color'" >> /etc/bash.bashrc
RUN echo  "alias l='ls -l'" >> /etc/bash.bashrc
RUN echo  "alias ll='ls -lh'" >> /etc/bash.bashrc
RUN echo  "alias la='ll -a'" >> /etc/bash.bashrc

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./project /project
WORKDIR /project

USER www-data
CMD python manage.py runserver 0.0.0.0:8000