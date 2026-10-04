from cart import add_item


def test_many_calls_are_independent():
    for item in ["a", "b", "c", "d"]:
        assert add_item(item) == [item]


def test_given_cart_is_modified_in_place():
    cart = []
    add_item("x", cart)
    add_item("y", cart)
    assert cart == ["x", "y"]
