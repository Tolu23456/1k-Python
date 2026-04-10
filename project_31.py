# Project 1 – Bank Account System
# Topic: Class & Functions
# Task: Create a BankAccount class with deposit, withdraw, and show_balance methods. Handle insufficient funds.
# Hints:

# Use attributes: balance

# Use conditionals to check withdrawals
# Example Output:

# Deposit: 1000
# Withdraw: 500
# Balance: 500

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def display(self):
        print(f"Display: {self.balance}")


ba1 = BankAccount(1000)
ba1.deposit(100)
ba1.withdraw(700)
ba1.display()
