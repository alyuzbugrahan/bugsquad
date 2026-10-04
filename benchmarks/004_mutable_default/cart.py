def add_item(item, cart=[]):
    """Add an item to the cart and return it. A new empty cart is used if none is given."""
    cart.append(item)
    return cart
