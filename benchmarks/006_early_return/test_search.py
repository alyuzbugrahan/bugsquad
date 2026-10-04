from search import find_first_negative


def test_negative_after_positive():
    assert find_first_negative([3, -1, -5]) == -1


def test_no_negatives():
    assert find_first_negative([1, 2]) is None


def test_negative_first():
    assert find_first_negative([-2]) == -2
