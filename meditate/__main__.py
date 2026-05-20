"""
Meditation app.
"""

import os
from typing import Union

import pyttsx3  # type: ignore
from langchain_openai import ChatOpenAI
from pydantic.types import SecretStr

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_API_URL = os.getenv("OPENAI_API_URL", "")
ENABLE_TTS = os.getenv("ENABLE_TTS", "1")

EXIT_TERMS = {"", "q", "Q", "exit"}

# Copied from `langchain_core.messages.BaseMessage`.
Content = Union[str, list[Union[str, dict]]]

SYSTEM_PROMPT = """Create a calming meditation experience to guide the user through a calm and detailed scene.
If it is a story, describe what happens in the story, if not a story then describe observations from the user perspective.

Give the user a choice of what to do with options as 1, 2, 3."""

USER_PROMPT = "Use the following input from the user: {input}"


def is_truthy(value: str) -> bool:
    """
    Parse common truthy and falsy strings.
    """
    return value.strip().lower() not in {"0", "false", "no", "off"}


def generate(model: ChatOpenAI, user_input: str) -> Content:
    """
    Send prompt to LLM and return result.
    """
    result = model.invoke(
        [
            ("system", SYSTEM_PROMPT),
            ("user", USER_PROMPT.format(input=user_input)),
        ]
    )

    return result.content


def start_loop(model: ChatOpenAI, engine: pyttsx3.Engine | None) -> None:
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
        print("Choose an option or enter custom text.")
        if engine is not None:
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
    engine: pyttsx3.Engine | None = None
    if is_truthy(ENABLE_TTS):
        engine = pyttsx3.init()
        engine.setProperty("rate", 140)

    start_loop(model, engine)


if __name__ == "__main__":
    main()
