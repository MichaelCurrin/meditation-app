"""Shared type aliases for the meditation app."""

from typing import Union

import pyttsx3  # type: ignore
from kokoro import KPipeline  # type: ignore

# Copied from `langchain_core.messages.BaseMessage`.
Content = Union[str, list[Union[str, dict]]]

# Selected speech engine. None means silent output.
Engine = pyttsx3.Engine | KPipeline | None
