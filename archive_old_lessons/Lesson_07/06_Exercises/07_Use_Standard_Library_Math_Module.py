import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Fundamental")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 07: Import the math module and use it to find the square root, the ceiling and the factorial of some numbers.
    """)
    return


@app.cell
def _():
    import math

    print(math.sqrt(49))
    print(math.ceil(4.2))
    print(math.factorial(5))
    return


if __name__ == "__main__":
    app.run()
