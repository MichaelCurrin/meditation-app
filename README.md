# Meditation app
> Python-based meditation app powered by LLM for content and text-to-speech output

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/meditation-app?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/meditation-app/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python->=3.12-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![dependency - poetry](https://img.shields.io/badge/dependency-poetry-blue?logo=poetry&logoColor=white)](https://pypi.org/project/poetry)

Instead of a pre-recorded guided meditation, you can create your own custom one and adapt it in real-time. It is interactive, so the AI gives you a scene and choices and you pick an option, like a text-based adventure video game.

To keep your journey and what your share **private**, configure the app to use a local LLM like Ollama. See OpenAI-related options [here](https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/artificial-intelligence/llm-api-urls.html).

## Limitations

- The voice is poor quality. It's possible to replace this using Kokoro like in this [demo](https://github.com/MichaelCurrin/kokoro-speech-demo) but this can be slow to be usable. Or use an API service, but that requires signup and subscription costs.
- The input is text and ideally it can listen to your voice.

## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
