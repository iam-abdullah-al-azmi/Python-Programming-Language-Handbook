---
title: OOP Principles Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Create a BankAccount class with a private balance. Provide deposit(), withdraw() and get_balance() methods, and do not allow withdrawing more than the balance.

```python {.marimo hide_code="true"}
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

account = BankAccount("Azmi", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(5000)
print(f"Balance: {account.get_balance()}")

try:
    print(account.__balance)
except AttributeError:
    print("Cannot access the private balance directly")
```