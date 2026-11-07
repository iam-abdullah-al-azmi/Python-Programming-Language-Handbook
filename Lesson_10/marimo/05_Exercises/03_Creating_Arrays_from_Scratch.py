import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="NumPy Foundations Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 03: Create arrays using zeros, ones, full and random.randint (seed the generator), then an array of even numbers from 2 to 18 with arange, 5 evenly spaced values between 2 and 20 with linspace and a 4x4 identity matrix. Print their shapes and values.
    """)
    return


@app.cell(hide_code=True)
def _():
    import numpy as np

    np.random.seed(42)
    print("zeros (2, 3):\n", np.zeros((2, 3)))
    print("ones (2, 3):\n", np.ones((2, 3)))
    print("full (3, 4) with 10:\n", np.full((3, 4), 10))

    _rand = np.random.randint(1, 10, (3, 4))
    print("random ints (3, 4):\n", _rand)
    print("shape:", _rand.shape)

    _even = np.arange(2, 20, 2)
    print("arange  :", _even, "| size:", _even.size)
    print("linspace:", np.linspace(2, 20, 5))
    print("identity 4x4:\n", np.eye(4, dtype=np.int64))
    return


if __name__ == "__main__":
    app.run()
