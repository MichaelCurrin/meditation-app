"""Kokoro speech engine helpers."""

import os
from typing import Optional

import sounddevice as sd  # type: ignore
import soundfile as sf  # type: ignore
from kokoro import KPipeline  # type: ignore


def create_kokoro_pipeline(repo_id: str) -> KPipeline:
    """
    Initialize and return a Kokoro pipeline.
    """
    return KPipeline(lang_code="a", repo_id=repo_id)


def process_kokoro_audio(
    audio: bytes, voice: str, output_dir: Optional[str] = None
) -> Optional[str]:
    """
    Process Kokoro audio data - either play directly or save to file.
    """
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"kokoro_{voice}.wav")
        sf.write(output_path, audio, 24000)
        print(f"Saved audio to: {output_path}")

        return output_path

    sd.play(audio, samplerate=24000)
    sd.wait()

    return None


def play_kokoro_audio(
    pipeline: KPipeline, text: str, voice: str, output_dir: Optional[str] = None
) -> None:
    """
    Synthesize and output audio for text using Kokoro.
    """
    generator = pipeline(text, voice=voice, speed=1, split_pattern=r"\n+")
    for _, _, audio in generator:
        process_kokoro_audio(audio, voice, output_dir)
