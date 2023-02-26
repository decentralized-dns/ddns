run:
	poetry run uvicorn ddnsapi.main:app --reload --date-header

fmt:
	poetry run black .

lint: fmt
	poetry run flake8 . --count --statistics

test: lint
	poetry run pytest

deploy:
	flyctl deploy
