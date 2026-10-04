from report import format_report


def test_small_prices():
    assert format_report(["10,50", "2,00"]) == "Total: 12.50 TL"


def test_price_above_one_thousand():
    assert format_report(["1.234,50"]) == "Total: 1234.50 TL"
