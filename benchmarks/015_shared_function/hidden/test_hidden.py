from display import display_phone
from phone import normalize_phone
from sms import sms_recipient


def test_sms_still_uses_e164():
    assert sms_recipient("0532 123 45 67") == "+905321234567"
    assert normalize_phone("05321234567") == "+905321234567"


def test_display_from_international_input():
    assert display_phone("+90 532 123 45 67") == "0532 123 45 67"


def test_display_other_number():
    assert display_phone("0216-555-01-23") == "0216 555 01 23"
