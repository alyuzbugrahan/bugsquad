from words import word_count


def test_case_insensitive():
    assert word_count("A a A b") == {"a": 3, "b": 1}


def test_single_word():
    assert word_count("one") == {"one": 1}


def test_all_unique():
    assert word_count("x y z") == {"x": 1, "y": 1, "z": 1}
