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
        Exercise 02: Create two 2x3 arrays and join them row-wise (axis=0) and column-wise (axis=1) using concatenate.
    """)
    return


@app.cell
def _():
    import numpy as np

    _a = np.array([[1, 2, 3], [4, 5, 6]])
    _b = np.array([[10, 20, 30], [40, 50, 60]])

    _rows = np.concatenate((_a, _b), axis=0)
    _cols = np.concatenate((_a, _b), axis=1)
    print("axis=0:\n", _rows, "\nshape:", _rows.shape)
    print("axis=1:\n", _cols, "\nshape:", _cols.shape)
    return


if __name__ == "__main__":
    app.run()
