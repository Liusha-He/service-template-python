from src.lib import extract_en


def test_find_entities_case1(entity_case1):
    text = entity_case1[0]
    entity_map = entity_case1[1]

    expected = {ent[0] for ent in entity_map}

    res = extract_en((text, ""), entity_map)

    assert res == expected
