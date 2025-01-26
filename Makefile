SHELL = /bin/bash

install:
	poetry install

fmt:
	poetry run black .
	poetry run isort .

run-llama:
	OPENAI_MODEL='llama3.2' OPENAI_API_KEY='dummy' OPENAI_API_URL='http://localhost:11434/v1' \
		poetry run python main.py

run-polli:
	OPENAI_API_URL='https://text.pollinations.ai/openai' poetry run main.py
