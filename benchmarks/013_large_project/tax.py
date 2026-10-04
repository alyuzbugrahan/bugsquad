VAT_RATE = 0.20


def add_vat(amount):
    """Return the amount including VAT."""
    return amount * (1 + VAT_RATE)
