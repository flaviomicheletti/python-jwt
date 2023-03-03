![image](https://user-images.githubusercontent.com/1257048/222756014-73f879fc-e806-4a17-a448-f8c6eae54b72.png)

# JWT with Python

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
