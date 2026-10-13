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
        Exercise 04: Create arrays using zeros, ones, full and random.randint (seed the generator) and print their shapes and values.
    """)
    return


@app.cell
def _():
    import numpy as np

    np.random.seed(42)
    print("zeros (2, 3):\n", np.zeros((2, 3)))
    print("ones (2, 3):\n", np.ones((2, 3)))
    print("full (3, 4) with 10:\n", np.full((3, 4), 10))

    _rand = np.random.randint(1, 10, (3, 4))
    print("random ints (3, 4):\n", _rand)
    print("shape:", _rand.shape)
    return


if __name__ == "__main__":
    app.run()
