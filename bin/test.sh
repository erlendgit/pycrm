#!/usr/bin/env bash

docker-compose exec web python manage.py test --keepdb "$@"