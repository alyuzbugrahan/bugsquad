from pytest import approx

from stats import average


def test_even_count():
    assert average([1, 2, 3, 4]) == approx(2.5)


def test_negative_numbers():
    assert average([-1, -2]) == approx(-1.5)


def test_single_value():
    assert average([5]) == 5


def test_floats():
    assert average([0.5, 0.25]) == approx(0.375)
