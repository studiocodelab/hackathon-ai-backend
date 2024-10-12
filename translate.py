# -*- coding: utf-8 -*-
"""Translation module using DeepL."""

import os
import deepl
import logging as lg


API_KEY = os.environ.get('DEEPL_API_KEY')
ENTRIES: dict[str, str] = {
    "you": "tobie",
}


def translate(text: str, target_lang: str) -> str:
    """Translate text to target language."""
    logger = lg.getLogger(f"{__name__}.{translate.__name__}")
    logger.info(f"Translating response to {target_lang} language.")
    translator = deepl.Translator(API_KEY)
    glossary_en_pl = translator.create_glossary(
        name="glossary",
        entries=ENTRIES,
        source_lang="EN-US",
        target_lang="PL",
    )
    glossary = glossary_en_pl if target_lang == "PL" else None
    logger.debug(f"Using glossary: {glossary}")
    return translator.translate_text(text, target_lang=target_lang, formality="more", glossary=glossary).text


if __name__ == "__main__":
    print(translate("Hello, World!"))

