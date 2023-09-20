install:
	cd app && pipenv install

dev-install:
	cd app && \
	pipenv install --dev && \
	pipenv run pre-commit install --hook-type pre-commit --hook-type pre-push

up:
	docker compose up -d

down:
	docker compose down

local-down:
	docker compose -f docker-compose.yml -f down

restart-build:
	docker compose down && docker compose up -d --build

rabbitmq-up:
	docker compose up -d rabbitmq

celery-beat:
	cd app && pipenv run celery -A bullish beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

celery-worker:
	cd app && pipenv run celery -A bullish worker -l info

celery-purge:
	cd app && pipenv run celery -A bullish purge -f

shell:
	cd app && pipenv run python manage.py shell

dev-server-up:
	cd app && pipenv run python manage.py runserver 0:8000

migrations:
	cd app && pipenv run python manage.py makemigrations

migrate:
	cd app && pipenv run python manage.py migrate

superuser:
	cd app && pipenv run python manage.py createsuperuser

up-build:
	docker compose -f docker-compose.yml up -d --build

test:
	cd app && pipenv run pytest

run-single-test:
	cd app && pipenv run pytest -k $(test)

test-coverage:
	cd app && pipenv run coverage erase
	rm -rf app/htmlcov
	cd app && pipenv run coverage run -m pytest
	cd app && pipenv run coverage html
