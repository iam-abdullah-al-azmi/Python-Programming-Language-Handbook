import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="NumPy Foundations Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 02: Create a 1D, a 2D and a 3D NumPy array and print the dimension, shape, size and data type of each one. Then create arrays from ints, from a mix of ints and floats and from a mix of ints and strings to show the upcasting, and convert an int16 array to int8 using astype.
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

    _ints = np.array([1, 2, 3])
    _mixed = np.array([1, 2.5, 3])
    _text = np.array([1, "A", 3.5])
    print(f"ints  : {_ints} -> {_ints.dtype}")
    print(f"mixed : {_mixed} -> {_mixed.dtype}")
    print(f"text  : {_text} -> {_text.dtype}")

    _small = np.array([1, 2, 3], dtype=np.int16)
    print(f"Before: {_small.dtype}")
    _small = _small.astype(np.int8)
    print(f"After : {_small.dtype}")
    return


if __name__ == "__main__":
    app.run()
