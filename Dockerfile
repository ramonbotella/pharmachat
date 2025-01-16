FROM python:3.12-slim

WORKDIR /root

# Install curl
RUN apt-get update && apt-get install -y curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -s ~/.local/share/pypoetry/venv/bin/poetry && \
    poetry config virtualenvs.create false

# Copy all your package in the root directory of your image.
COPY ./ /root/

# Install dependencies with Poetry
RUN poetry install

# Expose the API port
EXPOSE 8000

# Run the API
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
