from words import word_count


def test_repeated_word():
    assert word_count("the cat the") == {"the": 2, "cat": 1}


def test_empty_text():
    assert word_count("") == {}
