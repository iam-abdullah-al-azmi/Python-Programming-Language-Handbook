import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="NumPy Operations Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 01: Create a random 10x2 array (seed it), reshape it to 4x5, then flatten it row-wise and column-wise using ravel. Join two 2x3 arrays row-wise and column-wise using concatenate.
    """)
    return


@app.cell
def _():
    import numpy as np

    np.random.seed(1)
    _arr = np.random.randint(1, 100, size=(10, 2))
    print("Original shape:", _arr.shape)

    _reshaped = _arr.reshape(4, 5)
    print("Reshaped:\n", _reshaped)

    print("Row-wise flatten   :", np.ravel(_reshaped, "C"))
    print("Column-wise flatten:", np.ravel(_reshaped, "F"))
    print("flatten() ndim     :", _reshaped.flatten().ndim)

    _a = np.array([[1, 2, 3], [4, 5, 6]])
    _b = np.array([[10, 20, 30], [40, 50, 60]])
    _rows = np.concatenate((_a, _b), axis=0)
    _cols = np.concatenate((_a, _b), axis=1)
    print("axis=0:\n", _rows, "\nshape:", _rows.shape)
    print("axis=1:\n", _cols, "\nshape:", _cols.shape)
    return


if __name__ == "__main__":
    app.run()
