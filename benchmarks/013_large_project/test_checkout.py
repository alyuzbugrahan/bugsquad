from pytest import approx

from cart import Cart
from checkout import checkout


def test_small_cart_has_no_bulk_discount():
    cart = Cart()
    cart.add("mouse")
    # 150 * 1.2 VAT + 30 shipping
    assert checkout(cart) == approx(210.0)


def test_large_cart_gets_ten_percent_off():
    cart = Cart()
    cart.add("headset")
    # 600 - 60 discount = 540, * 1.2 VAT = 648, + 30 shipping
    assert checkout(cart) == approx(678.0)
