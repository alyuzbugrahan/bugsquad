from cart import add_item


def test_existing_cart_is_extended():
    cart = ["apple"]
    result = add_item("pear", cart)
    assert result == ["apple", "pear"]
    assert result is cart


def test_each_call_without_cart_starts_empty():
    assert add_item("apple") == ["apple"]
    assert add_item("pear") == ["pear"]
