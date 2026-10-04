from tax import add_tax


def invoice_total(items):
    """Return the total of (price, quantity) items, including tax, rounded to 2 decimals."""
    subtotal = sum(price * quantity for price, quantity in items)
    return round(add_tax(subtotal), 2)
