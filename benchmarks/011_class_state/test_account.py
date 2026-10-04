import pytest

from account import BankAccount, InsufficientFunds


def test_normal_withdrawal():
    acc = BankAccount(100)
    acc.withdraw(30)
    assert acc.balance == 70


def test_failed_withdrawal_keeps_balance():
    acc = BankAccount(50)
    with pytest.raises(InsufficientFunds):
        acc.withdraw(80)
    assert acc.balance == 50
