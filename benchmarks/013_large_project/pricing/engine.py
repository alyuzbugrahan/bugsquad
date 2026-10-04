from pricing.discount_rules import bulk_discount
from tax import add_vat


def price_order(subtotal):
    """Apply the bulk discount, then add VAT."""
    discounted = subtotal - bulk_discount(subtotal)
    return add_vat(discounted)
