#!/bin/bash
# .devcontainer/setup.sh

python -m venv /home/jovyan/default
source /home/jovyan/{env_name}/bin/activate
pip install poetry ipykernel pytest
poetry config virtualenvs.in-project true --local
poetry install --all-extras --with dev --with test
