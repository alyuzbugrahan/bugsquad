from summary import max_fahrenheit


def test_hottest_reading():
    assert max_fahrenheit([0, 100, 37]) == 212.0


def test_single_reading():
    assert max_fahrenheit([0]) == 32.0
