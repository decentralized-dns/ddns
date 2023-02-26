install:
	poetry install

lint:
	poetry run black .
	poetry run flake8 . --count --statistics

test: lint
	poetry run pytest
