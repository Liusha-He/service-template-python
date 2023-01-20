import pytest


@pytest.fixture()
def input_cases():
    return [
        (
            "I'm not sleapy and tehre is no place I'm giong to.",
            "im not sleepy and there is no place im going to",
        ),
        (
            "I like lemon juice and granuated sugar on my pancakes.",
            "i like lemon juice and granulated sugar on my pancakes",
        ),
    ]


@pytest.fixture()
def entity_case1():
    return (
        "i like lemon juice and granulated sugars on my pancake",
        [
            ("Lemon juice", ["lemon juice"]),
            ("Granulated sugars", ["granulated sugar", "granulated sugars"]),
            ("Pancakes", ["pancakes", "pancake"]),
        ],
    )
