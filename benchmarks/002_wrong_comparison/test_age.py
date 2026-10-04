from age import is_adult


def test_exactly_18_is_adult():
    assert is_adult(18) is True


def test_17_is_not_adult():
    assert is_adult(17) is False


def test_30_is_adult():
    assert is_adult(30) is True
