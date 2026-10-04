from pytest import approx

from cart import Cart
from checkout import checkout
from pricing.discount_rules import bulk_discount


def test_bulk_discount_amounts():
    assert bulk_discount(600) == approx(60)
    assert bulk_discount(1000) == approx(100)


def test_threshold_is_strict():
    assert bulk_discount(500) == approx(0)
    assert bulk_discount(400) == approx(0)


def test_large_order_end_to_end():
    cart = Cart()
    cart.add("monitor")
    # 3200 - 320 = 2880, * 1.2 = 3456, + 30 shipping
    assert checkout(cart) == approx(3486.0)
