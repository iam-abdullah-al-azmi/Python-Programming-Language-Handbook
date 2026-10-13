import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Fundamental")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 05: Convert a list of integers into a tuple and print its hash value.
    """)
    return


@app.cell
def _():
    integers = [1, 2]
    t = tuple(integers)
    print(f"Tuple: {t}")
    print(f"Hash: {hash(t)}")
    print(f"Same tuple, same hash: {hash(t) == hash((1, 2))}")
    return


if __name__ == "__main__":
    app.run()
