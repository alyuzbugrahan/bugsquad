class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw money. Raise InsufficientFunds if the balance is too low."""
        self.balance -= amount
        if self.balance < 0:
            raise InsufficientFunds(f"Cannot withdraw {amount}")
