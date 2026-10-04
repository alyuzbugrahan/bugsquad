from pytest import approx

from measurements import average_speed_kmh, kilometre_to_metre


def test_conversion_still_works():
    assert kilometre_to_metre(2) == approx(2000)


def test_one_kilometre_in_one_hour():
    assert average_speed_kmh(1000, 3600) == approx(1.0)
