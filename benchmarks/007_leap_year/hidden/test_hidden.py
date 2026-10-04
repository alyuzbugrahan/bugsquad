from calendar_utils import is_leap_year


def test_other_centuries():
    assert is_leap_year(2100) is False
    assert is_leap_year(1800) is False


def test_divisible_by_400():
    assert is_leap_year(1600) is True
    assert is_leap_year(2400) is True


def test_ordinary_years():
    assert is_leap_year(1996) is True
    assert is_leap_year(2001) is False
