import re
from typing import Tuple

from spellchecker import SpellChecker

from src.config import WORD_COUNT_DIR


def clean_text(text: str, local_dict: str = WORD_COUNT_DIR) -> Tuple[str, str]:
    """clean the input text bu using spell checker and remove punctuations, etc"""
    cleaned_text = text.lower()
    cleaned_text = cleaned_text.replace("-", " ")
    cleaned_text = re.sub(r"[^\w\s]", "", cleaned_text)

    checker_general = SpellChecker()
    checker_local = SpellChecker(
        local_dictionary=local_dict
    )  # note - here we only consider English

    new_words_local = []
    new_words_general = []

    for word in cleaned_text.split():
        word_local = word
        word_general = word

        if checker_general.unknown([word_local]):
            word_local = checker_local.correction(word_local)

        if checker_local.unknown([word_general]):
            word_general = checker_general.correction(word_general)

        new_words_local.append(word_local)
        new_words_general.append(word_general)

    return " ".join(new_words_local), " ".join(new_words_general)
