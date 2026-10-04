from pytest import approx

from calc import total


def test_longer_list():
    assert total([10, 20, 30, 40]) == 100


def test_negative_numbers():
    assert total([-1, 1, -5]) == -5


def test_floats():
    assert total([2.5, 2.5, 0.25]) == approx(5.25)


def test_empty():
    assert total([]) == 0
