import pytest
from pytest import approx

from measurements import average_speed_kmh, mile_to_kilometre, pound_to_kilogram


def test_running_pace():
    assert average_speed_kmh(10_000, 3000) == approx(12.0)


def test_highway():
    assert average_speed_kmh(100_000, 3600) == approx(100.0)


def test_rejects_non_positive_time():
    with pytest.raises(ValueError):
        average_speed_kmh(100, 0)


def test_other_functions_untouched():
    assert mile_to_kilometre(1) == approx(1.609344)
    assert pound_to_kilogram(1) == approx(0.45359237)
