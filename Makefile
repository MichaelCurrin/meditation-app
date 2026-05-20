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


app-help:
	poetry run python -m meditate -h


run: run-llama

RUN_CMD = poetry run python -m meditate
OLLAMA_VARS = OPENAI_MODEL='gemma3' OPENAI_API_KEY='dummy' OPENAI_API_URL='http://localhost:11434/v1'

run-llama:
	$(OLLAMA_VARS) $(RUN_CMD)

run-llama-kokoro:
	$(OLLAMA_VARS) $(RUN_CMD) --sound-model kokoro

run-llama-silent:
	$(OLLAMA_VARS) $(RUN_CMD)--sound-model none

run-llama-pyttsx3:
	$(OLLAMA_VARS) $(RUN_CMD) --sound-model pyttsx3


run-polli:
	OPENAI_API_URL='https://text.pollinations.ai/openai' \
		poetry run python -m meditate
