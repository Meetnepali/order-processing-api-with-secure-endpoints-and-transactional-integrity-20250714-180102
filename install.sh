#!/bin/sh
set -e

if ! command -v pip &>/dev/null; then
    echo "Please ensure pip (python3) is installed before proceeding." >&2
    exit 1
fi

pip install --no-cache-dir fastapi==0.109.0 uvicorn==0.23.2 sqlalchemy==2.0.15 pydantic==1.10.12 python-jose==3.3.0

if [ ! -d "app" ]; then
    echo "Error: 'app' directory not found. Make sure you are running install.sh from project root." >&2
    exit 1
fi
