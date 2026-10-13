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
        Exercise 05: Create an array of even numbers from 2 to 18 using arange, reshape it into 3x3, and create 5 evenly spaced values between 2 and 20 using linspace.
    """)
    return


@app.cell
def _():
    import numpy as np

    _even = np.arange(2, 20, 2)
    print("arange  :", _even, "| size:", _even.size)

    _matrix = _even.reshape(3, 3)
    print("reshaped:\n", _matrix)

    _spaced = np.linspace(2, 20, 5)
    print("linspace:", _spaced)
    return


if __name__ == "__main__":
    app.run()
