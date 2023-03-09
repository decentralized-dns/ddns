FROM python:3.11-alpine

WORKDIR /usr/src/app

ENV POETRY_VERSION=1.4.0

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# Install required system packages and install poetry
RUN apk add build-base && \
  apk add libffi-dev && \
  pip install poetry==$POETRY_VERSION

# Copy only requirements (caching in Docker layer)
WORKDIR /code
COPY pyproject.toml poetry.lock server.sh /code/

# Install dependencies
RUN poetry config virtualenvs.create false && \
	poetry install --only main --no-interaction --no-ansi --no-root

COPY ./ddnsapi /code/ddnsapi
COPY ./static /code/static
COPY ./templates /code/templates

# Configure the command
CMD ["/code/server.sh"]
