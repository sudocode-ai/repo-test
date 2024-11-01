#!/bin/bash

setup_environment() {
    conda deactivate || true  # The || true ensures the script continues even if conda isn't active
    python -m venv /home/jovyan/poetry_subproject
    source /home/jovyan/poetry_subproject/bin/activate
    cd poetry_subproject
    pip install poetry ipykernel pytest
    poetry config virtualenvs.create false --local
    poetry install --all-extras --with dev --with test || \
    poetry install --all-extras --with test || \
    poetry install --all-extras --with dev || \
    poetry install --all-extras

}

setup_environment