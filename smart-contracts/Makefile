install:
	poetry install

fmt:
	poetry run black .

lint: fmt
	poetry run flake8 . --count --statistics

test: lint
	poetry run pytest
