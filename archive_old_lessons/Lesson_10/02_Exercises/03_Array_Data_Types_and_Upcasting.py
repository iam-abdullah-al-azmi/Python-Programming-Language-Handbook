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
        Exercise 03: Create arrays from ints, from a mix of ints and floats and from a mix of ints and strings, then show how the data type is upcast. Finally convert an int16 array to int8 using astype.
    """)
    return


@app.cell
def _():
    import numpy as np

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
