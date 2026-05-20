"""
Meditation app.
"""

import argparse
from typing import Optional, cast

import pyttsx3  # type: ignore
from kokoro import KPipeline  # type: ignore
from langchain_openai import ChatOpenAI
from pydantic.types import SecretStr

from . import kokoro_engine, pyttsx3_engine
from meditate.constants import (
    EXIT_TERMS,
    OPENAI_API_KEY,
    OPENAI_API_URL,
    OPENAI_MODEL,
    SYSTEM_PROMPT,
    USER_PROMPT,
)
from meditate.types import Content, Engine


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


def play_audio(
    llm_result: Content,
    sound_model: str,
    engine: Engine,
    voice: str,
    output_dir: Optional[str],
) -> None:
    """
    Play or save audio using the selected sound model.
    """
    if sound_model == "none":
        return

    text = llm_result if isinstance(llm_result, str) else str(llm_result)

    if sound_model == "pyttsx3":
        if engine is not None:
            pyttsx3_engine.play_pyttsx3_audio(cast(pyttsx3.Engine, engine), text)
        return

    if engine is None:
        return

    kokoro_engine.play_kokoro_audio(cast(KPipeline, engine), text, voice, output_dir)


def start_loop(
    model: ChatOpenAI,
    sound_model: str,
    engine: Engine,
    voice: str,
    output_dir: Optional[str] = None,
) -> None:
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
        play_audio(llm_result, sound_model, engine, voice, output_dir)


def main() -> None:
    """
    Main command-line entry-point.
    """
    parser = argparse.ArgumentParser(description="Meditation app with text-to-speech")
    parser.add_argument(
        "--sound-model",
        choices=["pyttsx3", "kokoro", "none"],
        default="pyttsx3",
        help="Choose which sound model/backend to use.",
    )
    parser.add_argument(
        "--output-dir",
        help="Directory to save Kokoro audio files. If not provided, plays audio directly.",
        type=str,
    )
    parser.add_argument(
        "--voice",
        default="af_heart",
        help="Voice to use for Kokoro speech synthesis.",
        type=str,
    )
    parser.add_argument(
        "--kokoro-repo-id",
        default="hexgrad/Kokoro-82M",
        help="Kokoro model repository id.",
        type=str,
    )
    args = parser.parse_args()

    model = ChatOpenAI(
        model=OPENAI_MODEL,
        base_url=OPENAI_API_URL,
        api_key=SecretStr(OPENAI_API_KEY),
        max_completion_tokens=100,
    )

    engine: Engine = None

    if args.sound_model == "pyttsx3":
        engine = pyttsx3_engine.create_pyttsx3_engine(rate=140)
    elif args.sound_model == "kokoro":
        engine = kokoro_engine.create_kokoro_pipeline(repo_id=args.kokoro_repo_id)

    try:
        start_loop(model, args.sound_model, engine, args.voice, args.output_dir)
    except KeyboardInterrupt:
        print("\nStopping meditation.")


if __name__ == "__main__":
    main()
