from shipping import shipping_cost


def test_domestic():
    assert shipping_cost(1) == 30.0


def test_heavy_international():
    assert shipping_cost(12, "DE") == 100.0
