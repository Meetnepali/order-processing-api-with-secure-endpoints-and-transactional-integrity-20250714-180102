#!/bin/sh
set -e
./install.sh
echo "Starting FastAPI application on http://localhost:8000 ..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
