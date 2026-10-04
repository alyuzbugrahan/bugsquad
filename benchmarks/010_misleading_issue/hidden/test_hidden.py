from pytest import approx

from parsing import parse_price


def test_thousands_separator():
    assert parse_price("1.234,50") == approx(1234.5)


def test_millions():
    assert parse_price("12.345.678,90") == approx(12345678.9)


def test_plain_numbers():
    assert parse_price("7") == approx(7.0)
    assert parse_price("0,99") == approx(0.99)
