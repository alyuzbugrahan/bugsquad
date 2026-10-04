from pytest import approx

from convert import c_to_f
from summary import max_fahrenheit


def test_conversion_reference_points():
    assert c_to_f(100) == approx(212)
    assert c_to_f(-40) == approx(-40)
    assert c_to_f(37) == approx(98.6)


def test_negative_readings():
    assert max_fahrenheit([-10, -5, -20]) == approx(23.0)
