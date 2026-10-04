from pricing.engine import price_order
from shipping import shipping_cost


def checkout(cart, country="TR"):
    """Return the amount to charge: discounted subtotal plus VAT, plus shipping."""
    total = price_order(cart.subtotal()) + shipping_cost(cart.total_weight(), country)
    return round(total, 2)
