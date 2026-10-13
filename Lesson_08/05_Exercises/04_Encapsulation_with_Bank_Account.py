import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="OOP Principles")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 04: Create a BankAccount class with a private balance. Provide deposit(), withdraw() and get_balance() methods, and do not allow withdrawing more than the balance.
    """)
    return


@app.cell
def _():
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
    return


if __name__ == "__main__":
    app.run()
