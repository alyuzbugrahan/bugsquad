from catalog import get_product


class Cart:
    """A shopping cart holding product names and quantities."""

    def __init__(self):
        self.items = {}

    def add(self, name, quantity=1):
        self.items[name] = self.items.get(name, 0) + quantity

    def subtotal(self):
        """Sum of price * quantity, before discounts, tax and shipping."""
        return sum(get_product(n)[0] * q for n, q in self.items.items())

    def total_weight(self):
        return sum(get_product(n)[1] * q for n, q in self.items.items())
