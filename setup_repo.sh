#!/bin/bash

# Check if poetry is installed, if not, install it
if ! command -v poetry &> /dev/null
then
    echo "Poetry not found, installing..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
fi

# Run poetry install
poetry install

# Execute the Python script to set environment variables
python3 pharmachat/core/set_env.py

# Check if Docker is installed, if not, provide instructions
if ! command -v docker &> /dev/null
then
    echo "Docker not found. Please install Docker and Docker Compose."
    exit 1
fi

# Run docker compose up in detached mode
docker-compose up -d
