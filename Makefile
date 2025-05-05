SHELL = /bin/bash

install:
	poetry install

update:
	poetry update
update-force:
	poetry add langchain-openai@latest langchain-core@latest


fmt:
	poetry run black .
	poetry run isort .


run run-llama:
	OPENAI_MODEL='llama3.2' OPENAI_API_KEY='dummy' OPENAI_API_URL='http://localhost:11434/v1' \
		poetry run python -m meditate

run-polli:
	OPENAI_API_URL='https://text.pollinations.ai/openai' poetry run python -m meditate
