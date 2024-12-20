#!/bin/bash
poetry config virtualenvs.in-project true --local
poetry install --all-extras --with dev --with test || \
poetry install --all-extras --with test || \
poetry install --all-extras --with dev || \
poetry install --all-extras
