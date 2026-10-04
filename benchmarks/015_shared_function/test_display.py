from display import display_phone


def test_display_local_input():
    assert display_phone("05321234567") == "0532 123 45 67"


def test_display_spaced_input():
    assert display_phone("0532 123 45 67") == "0532 123 45 67"
