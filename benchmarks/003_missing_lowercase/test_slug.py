from slug import slugify


def test_two_words():
    assert slugify("Hello World") == "hello-world"


def test_surrounding_spaces():
    assert slugify("  python  ") == "python"


def test_three_words():
    assert slugify("Agentic AI Course") == "agentic-ai-course"
