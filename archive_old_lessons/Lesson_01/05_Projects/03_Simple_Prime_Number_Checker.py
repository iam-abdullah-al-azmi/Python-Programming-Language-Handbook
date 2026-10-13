import marimo

__generated_with = "0.23.14"
app = marimo.App()


@app.cell
def _():
    from math import pi, sqrt

    import marimo as mo

    return mo, pi


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project 03: Simple Prime Number Checker
    """)
    return


@app.cell
def _():
    val = eval(input("Enter a number: "))
    return (val,)


@app.cell
def _(val):
    flag = 0

    if val <= 1:
        print("Enter number more than 1")

    # for i in range(2, int(sqrt(val)) + 1):

    for i in range(2, int(val**0.5) + 1):
        if val % i == 0:
            flag = 1

    if flag == 0:
        print(f"{val} is a prime number")
    else:
        print(f"{val} is not a prime number")
    return


if __name__ == "__main__":
    app.run()
