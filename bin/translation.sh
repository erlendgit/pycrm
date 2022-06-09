#!/usr/bin/env bash

docker-compose exec web python manage.py makemessages -a
docker-compose exec web python manage.py compilemessages
