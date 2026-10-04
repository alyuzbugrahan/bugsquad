from search import find_first_negative


def test_negative_deep_in_list():
    assert find_first_negative([0, 4, 7, -3, -9]) == -3


def test_empty_list():
    assert find_first_negative([]) is None


def test_only_positives():
    assert find_first_negative([5, 6, 7]) is None


def test_float_negative():
    assert find_first_negative([10, -0.5]) == -0.5
