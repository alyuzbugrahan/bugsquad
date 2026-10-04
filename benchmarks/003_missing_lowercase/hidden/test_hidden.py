from slug import slugify


def test_mixed_case():
    assert slugify("MiXeD CaSe Title") == "mixed-case-title"


def test_single_word():
    assert slugify("Python") == "python"


def test_extra_spaces_between_words():
    assert slugify("  Leading   and trailing  ") == "leading-and-trailing"
