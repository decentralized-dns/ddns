#!/bin/sh

# Start python server
cd /code
uvicorn ddnsapi.main:app --host "0.0.0.0" --port 8080 --proxy-headers --date-header
