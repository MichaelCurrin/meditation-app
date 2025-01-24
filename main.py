"""
Meditation app.
"""

import os
from typing import Union

import pyttsx3
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic.types import SecretStr


OPENAI_MODEL = os.getenv("OPENAI_MODEL", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "dummy")
OPENAI_API_URL = os.getenv("OPENAI_API_URL", "http://localhost:1234/v1")

# Copied from `langchain_core.messages.BaseMessage`.
Content = Union[str, list[Union[str, dict]]]


def generate(model: ChatOpenAI, user_input: str) -> Content:
    prompt_template = PromptTemplate.from_template(
        "Create a calming meditation experience to guide the user through a calm and detailed scene. If it is a story, describe what happens in the story, if not a story then describe observations from the user perspective. Use the following input: {input}"
    )
    prompt = prompt_template.format(input=user_input)
    result = model.invoke(prompt)

    return result.content


def main() -> None:
    """Main command-line entry-point."""
    model = ChatOpenAI(
        model=OPENAI_MODEL,
        base_url=OPENAI_API_URL,
        api_key=SecretStr(OPENAI_API_URL),
        max_tokens=100,
    )
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    result = generate(
        model, "I walk through a misty forest on a mountain in the evening"
    )
    engine.say(result)
    engine.runAndWait()


if __name__ == "__main__":
    main()
