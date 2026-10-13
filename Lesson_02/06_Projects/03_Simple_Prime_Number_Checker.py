import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Projects")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Project 03: Simple Prime Number Checker
    Take a number from the user and check whether it is prime by testing every possible divisor up to its square root.
    """)
    return


@app.cell
def _():
    val = eval(input("Enter a number: "))

    return (val,)


@app.cell
def _(val):
    is_prime = True
    if val <= 1:
        print("Enter number more than 1")
        is_prime = False
    else:
        for i in range(2, int(val**0.5) + 1):
            if val % i == 0:
                is_prime = False
                break

    if val > 1:
        if is_prime:
            print(f"{val} is a prime number")
        else:
            print(f"{val} is not a prime number")
    return


if __name__ == "__main__":
    app.run()
