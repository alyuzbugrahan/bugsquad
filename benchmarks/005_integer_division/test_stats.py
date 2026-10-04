from stats import average


def test_average_with_fraction():
    assert average([1, 2]) == 1.5


def test_average_whole_number():
    assert average([2, 4, 6]) == 4
