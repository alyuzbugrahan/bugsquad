from calendar_utils import is_leap_year


def test_regular_leap_year():
    assert is_leap_year(2024) is True


def test_regular_common_year():
    assert is_leap_year(2023) is False


def test_century_year_is_not_leap():
    assert is_leap_year(1900) is False


def test_year_divisible_by_400_is_leap():
    assert is_leap_year(2000) is True
