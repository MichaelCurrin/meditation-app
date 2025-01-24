SHELL = /bin/bash

install:
	poetry install

fmt:
	poetry run black .
	poetry run isort .
