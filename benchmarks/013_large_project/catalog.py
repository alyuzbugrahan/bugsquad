"""Product catalog: name -> (price in TL, weight in kg)."""

PRODUCTS = {
    "keyboard": (450.0, 1.2),
    "mouse": (150.0, 0.2),
    "monitor": (3200.0, 5.5),
    "cable": (50.0, 0.1),
    "headset": (600.0, 0.4),
}


def get_product(name):
    """Return (price, weight) for a product name."""
    return PRODUCTS[name]
