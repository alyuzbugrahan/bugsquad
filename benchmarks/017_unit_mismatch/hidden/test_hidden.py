from pytest import approx

from report import format_report
from stats import average_seconds
from timeout import is_timed_out
from timing import elapsed_ms


def test_elapsed_is_in_milliseconds():
    assert elapsed_ms(1000, 3500) == 2500


def test_average_works_in_seconds():
    assert average_seconds([1.0, 2.0]) == approx(1.5)


def test_timeout_still_uses_milliseconds():
    assert is_timed_out(0, 2000, 1500) is True
    assert is_timed_out(0, 1000, 1500) is False


def test_report_other_values():
    assert format_report([(0, 250), (0, 750)]) == "Average: 0.5 s"
