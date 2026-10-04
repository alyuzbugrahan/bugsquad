def shipping_cost(weight_kg, country="TR"):
    """Flat shipping fee per country, plus a surcharge for parcels heavier than 10 kg."""
    base = 30.0 if country == "TR" else 80.0
    if weight_kg > 10:
        base += 20.0
    return base
