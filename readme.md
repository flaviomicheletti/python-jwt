# JWT

# Instalation

    python3 -m venv .venv && . .venv/bin/activate

## Install

In both environments you will need to install it only once.

    pip install -U pytest
    pip install pytest-mock
    pip install requests

## Running

    pytest


## Coverage

    coverage run -m pytest
    coverage html

    pytest --cov . --cov-report html
