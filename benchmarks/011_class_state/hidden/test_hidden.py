import pytest

from account import BankAccount, InsufficientFunds


def test_withdraw_entire_balance():
    acc = BankAccount(40)
    acc.withdraw(40)
    assert acc.balance == 0


def test_repeated_failures_do_not_change_balance():
    acc = BankAccount(10)
    for _ in range(3):
        with pytest.raises(InsufficientFunds):
            acc.withdraw(25)
    assert acc.balance == 10


def test_deposit_after_failure():
    acc = BankAccount(5)
    with pytest.raises(InsufficientFunds):
        acc.withdraw(6)
    acc.deposit(10)
    assert acc.balance == 15
