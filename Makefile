SHELL = /bin/bash

all: install

h help:
	@grep '^[a-z]' Makefile


install:
	poetry install

update:
	poetry update
update-force:
	poetry add langchain-openai@latest langchain-core@latest


fmt:
	poetry run black .
	poetry run isort .

run: run-llama

run-llama:
	OPENAI_MODEL='gemma3' \
	OPENAI_API_KEY='dummy' \
	OPENAI_API_URL='http://localhost:11434/v1' \
		poetry run python -m meditate

run-silent:
	ENABLE_TTS='0' $(MAKE) run

run-polli:
	OPENAI_API_URL='https://text.pollinations.ai/openai' \
		poetry run python -m meditate
