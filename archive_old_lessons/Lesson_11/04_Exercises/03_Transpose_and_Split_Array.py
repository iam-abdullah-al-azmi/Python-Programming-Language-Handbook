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
        Exercise 03: Create the numbers 10 to 100 (10 values) with linspace, reshape to 2x5, transpose it, and split the result into 3 parts using array_split.
    """)
    return


@app.cell
def _():
    import numpy as np

    _arr = np.linspace(10, 100, 10, dtype=np.int64).reshape(2, 5)
    print("Original:\n", _arr)

    _t = np.transpose(_arr)
    print("Transposed:\n", _t)

    for _i, _part in enumerate(np.array_split(_t, 3), 1):
        print(f"Part {_i}:\n", _part)
    return


if __name__ == "__main__":
    app.run()
