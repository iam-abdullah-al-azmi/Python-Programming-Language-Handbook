import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="NumPy Operations Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 03: Sort a 2D array along each axis, then use where, argmax and argmin to find positions of values greater than 8 and the largest and smallest elements. Finally generate 100 random numbers (seed it), count how many are greater than 40 and check with all and any whether every value is above 0 or any value is above 98.
    """)
    return


@app.cell(hide_code=True)
def _():
    import numpy as np

    _arr = np.array([[3, 2, 8, 5], [45, 23, 9, 32]])
    print("Sort axis=1:\n", np.sort(_arr, axis=1))
    print("Sort axis=0:\n", np.sort(_arr, axis=0))

    print("Indexes of values > 8:", np.where(_arr > 8))
    print("Values > 8 kept, others 0:\n", np.where(_arr > 8, _arr, 0))
    print("argmax:", np.argmax(_arr), "| argmin:", np.argmin(_arr))

    np.random.seed(7)
    _numbers = np.random.randint(1, 100, 100)
    print("Greater than 40:", np.count_nonzero(_numbers > 40))
    print("All values > 0 :", np.all(_numbers > 0))
    print("Any value > 98 :", np.any(_numbers > 98))
    return


if __name__ == "__main__":
    app.run()
