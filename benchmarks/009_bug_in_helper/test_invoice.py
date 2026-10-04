from invoice import invoice_total


def test_single_item():
    assert invoice_total([(10.0, 2)]) == 24.0


def test_empty_invoice():
    assert invoice_total([]) == 0.0
