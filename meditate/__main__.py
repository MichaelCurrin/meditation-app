"""
Meditation app.
"""

import os
from typing import Union

import pyttsx3  # type: ignore
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic.types import SecretStr


OPENAI_MODEL = os.getenv("OPENAI_MODEL", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_API_URL = os.getenv("OPENAI_API_URL", "")

EXIT_TERMS = {"", "q", "Q", "exit"}

# Copied from `langchain_core.messages.BaseMessage`.
Content = Union[str, list[Union[str, dict]]]


def generate(model: ChatOpenAI, user_input: str) -> Content:
    """
    Send prompt to LLM and return result.
    """
    prompt_template = PromptTemplate.from_template(
        "Create a calming meditation experience to guide the user through a"
        " calm and detailed scene. If it is a story, describe what happens in"
        " the story, if not a story then describe observations from the user"
        " perspective. Use the following input: {input}"
    )
    prompt = prompt_template.format(input=user_input)
    result = model.invoke(prompt)

    return result.content


def start_loop(model: ChatOpenAI, engine: pyttsx3.Engine) -> None:
    initialized = False

    print(
        "Starting meditation. When prompted for input, give an empty"
        ' response or "q" to exit.'
    )

    while True:
        if initialized:
            user_input = input("> ")
            if user_input in EXIT_TERMS:
                break
        else:
            user_input = "Give a welcome to start the meditation"
            initialized = True

        llm_result = generate(model, user_input)
        print(llm_result)
        engine.say(llm_result)
        engine.runAndWait()


def main() -> None:
    """
    Main command-line entry-point.
    """
    model = ChatOpenAI(
        model=OPENAI_MODEL,
        base_url=OPENAI_API_URL,
        api_key=SecretStr(OPENAI_API_URL),
        max_completion_tokens=100,
    )
    engine = pyttsx3.init()
    engine.setProperty("rate", 140)

    start_loop(model, engine)


if __name__ == "__main__":
    main()
