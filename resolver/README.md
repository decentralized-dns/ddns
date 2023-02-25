# API

API is using fastapi and uvicorn.

## How to run locally

```sh
$ poetry install
$ poetry run uvicorn --app-dir api main:app --reload
```

```sh
$ curl http://127.0.0.1:8000
{"message":"Hello DDNS"}
```
