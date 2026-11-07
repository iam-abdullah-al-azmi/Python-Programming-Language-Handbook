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
    Exercise 02: Add, subtract, multiply and divide two arrays element-wise, then square a 2x5 array and add a 1D array to it using broadcasting.
    """)
    return


@app.cell(hide_code=True)
def _():
    import numpy as np

    _a = np.array([1, 2, 3, 4, 5])
    _b = np.array([6, 7, 8, 9, 10])
    print("add     :", _a + _b)
    print("subtract:", _a - _b)
    print("multiply:", _a * _b)
    print("divide  :", np.round(_a / _b, 3))

    _matrix = np.arange(1, 11).reshape(2, 5) ** 2
    print("Squared 2x5:\n", _matrix)
    print("Broadcast add:\n", _matrix + _a)
    return


if __name__ == "__main__":
    app.run()
