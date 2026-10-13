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
        Exercise 05: Sort a 2D array along each axis, then use where, argmax and argmin to find positions of values greater than 8 and the largest and smallest elements.
    """)
    return


@app.cell
def _():
    import numpy as np

    _arr = np.array([[3, 2, 8, 5], [45, 23, 9, 32]])
    print("Sort axis=1:\n", np.sort(_arr, axis=1))
    print("Sort axis=0:\n", np.sort(_arr, axis=0))

    print("Indexes of values > 8:", np.where(_arr > 8))
    print("Values > 8 kept, others 0:\n", np.where(_arr > 8, _arr, 0))
    print("argmax:", np.argmax(_arr), "| argmin:", np.argmin(_arr))
    return


if __name__ == "__main__":
    app.run()
