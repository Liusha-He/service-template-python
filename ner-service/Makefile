SHELL := /bin/sh

build:
	pip install poetry && poetry install

unit-test:
	poetry run pytest tests

integration:
	docker-compose -f local-compose.yaml up -d --force-recreate && \
	poetry run coverage run -m pytest integration && \
	docker-compose -f local-compose.yaml down

lint:
	poetry run flake8 .

format:
	poetry run black src tests

ci-format:
	poetry run black src --check

run:
	poetry run python nltk_data_init.py && \
	poetry run python -m src.main
