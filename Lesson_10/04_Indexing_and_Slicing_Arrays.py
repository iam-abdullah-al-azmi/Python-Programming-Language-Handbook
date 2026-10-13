import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="NumPy Foundations")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Indexing and Slicing Arrays
    Learn how to read and change single elements of an array with indexes and how to take parts of an array with slices.
    """)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Indexing
    An index picks one element, starting from 0. In a 2D array the first index selects the row and the second the column. Assigning to an index changes the element.
    """)
    return


@app.cell
def _(np):
    array_one = np.arange(5)
    array_two = np.array([np.arange(5), np.arange(5)])
    print(array_one.shape, array_two.shape)

    array_one[2] = 10
    print(array_one)

    array_two[0][2] = 84
    print(array_two)

    return array_one, array_two


@app.cell
def _(mo):
    mo.md(r"""
    ## Slicing
    A slice `start:stop:step` takes a range of elements (the stop index is not included). For a 2D array give one slice for the rows and one for the columns, separated by a comma.
    """)
    return


@app.cell
def _(array_one, array_two):
    array_one_1 = array_one[1:4]
    print(array_one_1)

    array_two_1 = array_two[0:1:1, 0::1]
    print(array_two_1)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## More ways to select elements
    - negative indexes count from the end (`-1` is the last element)
    - `arr[row, column]` is a shorter way to write `arr[row][column]`
    - a single `:` selects the whole dimension
    - a condition such as `arr > 5` creates a boolean mask that selects only the matching elements
    """)
    return


@app.cell
def _(np):
    _matrix = np.arange(1, 13).reshape(3, 4)
    print(_matrix)

    print(_matrix[-1])  # last row
    print(_matrix[1, 2])  # same as _matrix[1][2]
    print(_matrix[:, 0])  # first column
    print(_matrix[0:2, 1:3])  # rows 0-1 and columns 1-2
    print(_matrix[_matrix > 8])  # boolean mask
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## A slice is a view, not a copy
    A slice shares its memory with the original array, so changing the slice changes the original. Use `copy()` when you need an independent array.
    """)
    return


@app.cell
def _(np):
    _original = np.arange(5)
    _view = _original[1:4]
    _view[0] = 99
    print(_original)

    _copy = _original[1:4].copy()
    _copy[0] = -1
    print(_original, _copy)
    return


if __name__ == "__main__":
    app.run()
