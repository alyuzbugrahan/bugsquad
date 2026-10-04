from report import format_report


def test_average_report():
    runs = [(0, 1000), (5000, 7000)]
    assert format_report(runs) == "Average: 1.5 s"
