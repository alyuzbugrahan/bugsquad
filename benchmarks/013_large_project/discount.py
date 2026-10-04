"""Discount helpers for the admin panel."""


def bulk_discount(subtotal, percent=10):
    """Return percent percent of the subtotal."""
    return subtotal * percent / 100


def staff_discount(subtotal):
    return subtotal * 0.25
