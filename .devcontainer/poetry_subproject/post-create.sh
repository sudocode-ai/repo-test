#!/bin/bash
# source /opt/conda/etc/profile.d/conda.sh
# conda deactivate || true  # The || true ensures the script continues even if conda isn't active
python -m venv /home/jovyan/poetry_subproject
source /home/jovyan/poetry_subproject/bin/activate

# Verify we're in the correct virtual environment
echo "Using Python from: $(which python)"
echo "Python version: $(python --version)"

cd poetry_subproject
pip install pytest
poetry install --all-extras --with dev --with test || \
poetry install --all-extras --with test || \
poetry install --all-extras --with dev || \
poetry install --all-extras
