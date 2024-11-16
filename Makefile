install:
	poetry install

fix:
	black .
	isort .
