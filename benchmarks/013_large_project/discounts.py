"""Coupon codes."""

COUPONS = {"WELCOME10": 10, "SUMMER25": 25}


def coupon_amount(code, subtotal):
    """Return the TL amount a coupon takes off, or 0 for unknown codes."""
    percent = COUPONS.get(code.upper(), 0)
    return subtotal * percent / 100
