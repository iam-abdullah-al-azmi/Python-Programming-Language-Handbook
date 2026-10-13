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
        Exercise 01: Create a 1D, a 2D and a 3D NumPy array and print the dimension, shape, size and data type of each one.
    """)
    return


@app.cell
def _():
    import numpy as np

    _one = np.array([1, 2, 3, 4, 5])
    _two = np.array([[1, 2, 3], [4, 5, 6]])
    _three = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    for _name, _arr in [("1D", _one), ("2D", _two), ("3D", _three)]:
        print(f"{_name} -> ndim: {_arr.ndim} | shape: {_arr.shape} | size: {_arr.size} | dtype: {_arr.dtype}")
    return


if __name__ == "__main__":
    app.run()
