from pytest import approx

from invoice import invoice_total
from tax import add_tax


def test_add_tax_directly():
    assert add_tax(100) == approx(120)
    assert add_tax(0) == approx(0)


def test_several_items():
    assert invoice_total([(5.0, 3), (2.5, 2)]) == approx(24.0)
