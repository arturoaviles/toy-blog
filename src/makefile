build:
	docker-compose build

up:
	docker-compose up

ssh:
	docker exec toy-blog -it /bin/bash

server:
	docker exec toy-blog -it python manage.py runserver 0.0.0.0:8000

down:
	docker-compose down

flake8:
	flake8 .

test:
	./manage.py test

run:
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py makemigrations; python manage.py migrate

superuser:
	python manage.py createsuperuser