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
        Exercise 04: Create a 3x4 array with arange, change one element, then print the first row, the last column and the 2x2 block in the top-left corner.
    """)
    return


@app.cell
def _():
    import numpy as np

    _arr = np.arange(1, 13).reshape(3, 4)
    print("Original:\n", _arr)

    _arr[1][2] = 100
    print("After changing row 1, column 2 to 100:\n", _arr)

    print("First row   :", _arr[0])
    print("Last column :", _arr[:, -1])
    print("Top-left 2x2:\n", _arr[0:2, 0:2])
    return


if __name__ == "__main__":
    app.run()
