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
        Exercise 01: Create a random 10x2 array (seed it), reshape it to 4x5, then flatten it row-wise and column-wise using ravel.
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
    return


if __name__ == "__main__":
    app.run()
