# -*- coding: utf-8 -*-
"""Translation module using DeepL."""

import os
import deepl


API_KEY = os.environ.get('DEEPL_API_KEY')
ENTRIES: dict[str, str] = {
    "you": "tobie",
}


def translate(text: str, target_lang: str = "PL") -> str:
    """Translate text to target language."""
    translator = deepl.Translator(API_KEY)
    glossary = translator.create_glossary(
        name="glossary",
        entries=ENTRIES,
        target_lang=target_lang,
    )
    return translator.translate_text(text, target_lang=target_lang, formality="more")


if __name__ == "__main__":
    print(translate("Hello, World!"))

