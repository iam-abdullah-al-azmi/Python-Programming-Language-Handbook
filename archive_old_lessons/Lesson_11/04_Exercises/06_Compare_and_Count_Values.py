import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 06: Generate 100 random numbers (seed it), count how many are greater than 40 and check with all and any whether every value is above 0 or any value is above 98.
    """)
    return


@app.cell
def _():
    import numpy as np

    np.random.seed(7)
    _arr = np.random.randint(1, 100, 100)

    print("Greater than 40:", np.count_nonzero(_arr > 40))
    print("All values > 0 :", np.all(_arr > 0))
    print("Any value > 98 :", np.any(_arr > 98))
    return


if __name__ == "__main__":
    app.run()
