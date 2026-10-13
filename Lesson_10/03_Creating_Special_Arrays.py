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
    # Creating Special Arrays
    Learn how to build arrays from scratch: filled with zeros, ones or a chosen value, random numbers, number ranges, and identity or diagonal matrices.
    """)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Zeros, ones and the like functions
    `np.zeros` and `np.ones` take the shape as a tuple. `np.zeros_like` and `np.ones_like` copy the shape of an existing array.
    """)
    return


@app.cell
def _(np):
    array_template = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

    array_twelve = np.zeros((2, 3))
    print(array_twelve, array_twelve.dtype)

    array_thirteen = np.zeros_like(array_template)
    print(array_thirteen, array_thirteen.dtype, array_thirteen.shape, array_template.shape)

    array_fourteen = np.ones((2, 3))
    array_fifteen = np.ones_like(array_thirteen)
    print(array_fourteen.shape, array_fifteen.shape)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Empty and full arrays
    `np.empty` only reserves the memory, so the values you see are whatever was there before and can be anything.
    `np.full` fills the array with a chosen value.
    """)
    return


@app.cell
def _(np):
    array_sixteen = np.empty((3, 4))
    print(array_sixteen)

    array_seventeen = np.full((3, 4), 10)
    print(array_seventeen)

    array_seventeen = np.full((3, 4), True)
    print(array_seventeen)

    array_seventeen = np.full((3, 4), np.inf)
    print(array_seventeen)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Random arrays
    `np.random.seed()` makes the random numbers repeatable. `rand` gives floats between 0 and 1, `randint(low, high, size)` gives integers from `low` up to but not including `high`, and `uniform(low, high, size)` gives floats between two values.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    array_eighteen = np.random.rand(3, 4)
    print(array_eighteen, array_eighteen.dtype)

    array_eighteen = np.random.randint(3, 5)
    print(array_eighteen)

    array_eighteen = np.random.randint(3, 5, 10)
    print(array_eighteen)

    array_eighteen = np.random.randint(3, 5, (10, 5))
    print(array_eighteen)
    return


@app.cell
def _(np):
    array_nineteen = np.random.uniform(3, 10, (3, 4))
    print(array_nineteen, array_nineteen.dtype)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Ranges: arange, linspace and logspace
    - `np.arange(start, stop, step)` works like `range` but returns an array
    - `np.linspace(start, stop, count)` gives `count` evenly spaced values, including the stop value
    - `np.logspace(start, stop, count)` gives values spaced evenly on a log scale (powers of 10 by default)

    The `reshape` method changes the shape of an array without changing its values; it is explained in the next lesson.
    """)
    return


@app.cell
def _(np):
    # array creation with range function
    array_twenty = np.arange(2, 20, 2)
    print(array_twenty, array_twenty.dtype, array_twenty.size)

    array_twenty = array_twenty.reshape(3, 3)
    print(array_twenty, array_twenty.dtype, array_twenty.size)

    # array creation with linspace (linear space)
    array_twenty_one = np.linspace(2, 20, 5, retstep=False)
    print(array_twenty_one, array_twenty_one.dtype, array_twenty_one.shape)

    # array creation with logspace
    array_twenty_two = np.logspace(0, 4, 5)
    print(array_twenty_two)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Matrices for linear algebra
    `np.diag` puts a list on the diagonal of a square matrix. `np.eye(rows, columns, k)` creates ones on a diagonal and zeros elsewhere; `k` shifts the diagonal (negative is below the main one).
    """)
    return


@app.cell
def _(np):
    array_twenty_three = np.diag([1, 2, 3, 4, 5])
    print(array_twenty_three)

    array_twenty_four = np.eye(4, dtype=np.int64)
    print(array_twenty_four)

    array_twenty_four = np.eye(3, 4, dtype=np.int64)
    print(array_twenty_four)

    array_twenty_four = np.eye(3, 4, -1, dtype=np.int64)
    print(array_twenty_four)
    return


if __name__ == "__main__":
    app.run()
