"""Shared constants and configuration for the meditation app."""

import os

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_API_URL = os.getenv("OPENAI_API_URL", "")

EXIT_TERMS = {"", "q", "Q", "exit"}

SYSTEM_PROMPT = """Create a calming meditation experience to guide the user through a calm and detailed scene.
If it is a story, describe what happens in the story, if not a story then describe observations from the user perspective.

Give the user a choice of what to do with options as 1, 2, 3."""

USER_PROMPT = "Use the following input from the user: {input}"