run:
	poetry run uvicorn ddnsapi.main:app --reload --date-header --ssl-keyfile ../dev/ddns.dev-key.pem --ssl-certfile ../dev/ddns.dev.pem

test:
	poetry run pytest

deploy:
	flyctl deploy
