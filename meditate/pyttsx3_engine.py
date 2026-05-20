"""pyttsx3 speech engine helpers.

Low quality but quick and also easy to run without saving a file."""

import pyttsx3  # type: ignore


def create_pyttsx3_engine(rate: int = 140) -> pyttsx3.Engine:
    """
    Initialize and configure a pyttsx3 engine.
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    return engine


def play_pyttsx3_audio(engine: pyttsx3.Engine, text: str) -> None:
    """
    Speak text using a pyttsx3 engine.
    """
    engine.say(text)
    engine.runAndWait()
