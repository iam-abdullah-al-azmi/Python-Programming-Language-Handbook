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
        Exercise 06: Create a diagonal matrix from the list [1, 2, 3, 4, 5], a 4x4 identity matrix and a 3x4 matrix with ones on the diagonal below the main one.
    """)
    return


@app.cell
def _():
    import numpy as np

    print("diag:\n", np.diag([1, 2, 3, 4, 5]))
    print("identity 4x4:\n", np.eye(4, dtype=np.int64))
    print("eye 3x4 shifted by -1:\n", np.eye(3, 4, -1, dtype=np.int64))
    return


if __name__ == "__main__":
    app.run()
