import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="NumPy Operations")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Reshaping, Joining and Splitting Arrays
    Learn how to change the shape of an array, flatten it, transpose it, join arrays together and split an array into parts.
    """)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Reshape
    `reshape(rows, columns)` gives the same values a new shape; the total number of elements must stay the same (10 x 2 = 4 x 5).
    A common layout in data science is one row per sample and one column per feature.
    """)
    return


@app.cell
def _(np):
    np.random.seed(1)
    array_one = np.random.randint(1, 100, size=(10, 2))  # 10 samples and 2 features
    print(f"{len(array_one)}\n{array_one}\n{array_one.shape}")

    return (array_one,)


@app.cell
def _(array_one):
    array_one_1 = array_one.reshape(4, 5)
    print(f"{len(array_one_1)}\n{array_one_1}\n{array_one_1.shape}")

    return (array_one_1,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Flattening
    `ravel` and `flatten` turn an array into 1D. The order `"C"` reads row by row and `"F"` reads column by column.
    `flatten()` always returns a copy while `ravel()` returns a view when it can.
    """)
    return


@app.cell
def _(array_one_1, np):
    array_one_col_flat = np.ravel(array_one_1, "F")  # This will flatten the matrix column wise
    print(array_one_col_flat)
    array_one_row_flat = np.ravel(array_one_1, "C")  # This will flatten the matrix row wise
    print(array_one_row_flat)

    array_one_2 = array_one_1.flatten()
    print(array_one_2, array_one_2.ndim)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Concatenation
    `np.concatenate` joins arrays along an axis: `axis=0` stacks them row wise (one below the other) and `axis=1` joins them column wise (side by side).
    """)
    return


@app.cell
def _(np):
    array_two = np.random.randint(1, 15, size=(6, 7))
    array_three = np.random.randint(20, 35, size=(6, 7))

    array_two_plus_three = np.concatenate((array_two, array_three), axis=0)  # row wise concatenation
    print(array_two_plus_three, array_two_plus_three.shape)

    array_two_plus_three = np.concatenate((array_two, array_three), axis=1)  # column wise concatenation
    print(array_two_plus_three, array_two_plus_three.shape)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Transpose
    Transposing swaps rows and columns, so a 2 x 5 array becomes 5 x 2.
    """)
    return


@app.cell
def _(np):
    array_three_1 = np.linspace(10, 100, 10, dtype=np.int64)
    array_three_1 = array_three_1.reshape(2, 5)
    print(array_three_1)
    array_three_1 = np.transpose(array_three_1)
    print(array_three_1)

    return (array_three_1,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Splitting
    `np.split` needs the array to divide into equal parts, otherwise it raises a `ValueError`. `np.array_split` allows unequal parts.
    """)
    return


@app.cell
def _(array_three_1, np):
    try:
        np.split(array_three_1, 3)  # 5 rows cannot be divided into 3 equal parts
    except ValueError as _error:
        print(f"ValueError: {_error}")

    array_four = np.array_split(array_three_1, 3)
    print(array_four)
    return


if __name__ == "__main__":
    app.run()
