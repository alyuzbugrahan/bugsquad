BULK_THRESHOLD = 500
BULK_PERCENT = 10


def bulk_discount(subtotal):
    """Return the discount amount: BULK_PERCENT percent for orders strictly above BULK_THRESHOLD TL."""
    if subtotal > BULK_THRESHOLD:
        return subtotal * BULK_PERCENT / 1000
    return 0.0
