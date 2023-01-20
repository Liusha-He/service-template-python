import os

from src.handler import clean_text


TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_data")


def test_input_handler_in_some_cases(input_cases):
    for i, expected in input_cases:
        res = clean_text(i, os.path.join(TEST_DATA_DIR, "word_counts.json"))

        assert expected in res
