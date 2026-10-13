import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="NumPy Operations Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 04: Save a small 2D array to a temporary CSV text file with savetxt and read it back with genfromtxt.
    """)
    return


@app.cell(hide_code=True)
def _():
    import tempfile
    from pathlib import Path

    import numpy as np

    _data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    with tempfile.TemporaryDirectory() as _folder:
        _path = Path(_folder) / "numbers.txt"
        np.savetxt(_path, _data, delimiter=",", fmt="%d")
        _loaded = np.genfromtxt(_path, delimiter=",")

    print("Loaded array:\n", _loaded)
    print("Shape:", _loaded.shape)
    return


if __name__ == "__main__":
    app.run()
