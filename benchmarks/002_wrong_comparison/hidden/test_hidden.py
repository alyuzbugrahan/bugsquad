from age import is_adult


def test_boundary_values():
    assert is_adult(17) is False
    assert is_adult(18) is True
    assert is_adult(19) is True


def test_far_from_boundary():
    assert is_adult(0) is False
    assert is_adult(100) is True
