# complex_program.py

class BankAccount:
    """Class representing a bank account."""

    def __init__(self, account_number, balance=0):
        """Initialize the bank account with an account number and optional initial balance."""
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposit funds into the account."""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw funds from the account if sufficient balance is available."""
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_balance(self):
        """Get the current balance of the account."""
        return self.balance
