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
        Exercise 02: Find the common elements of two lists using the set intersection() method.
    """)
    return


@app.cell
def _():
    list_a = [1, 2, 3, 4, 5, 6]
    list_b = [4, 5, 6, 7, 8, 9]
    common = set(list_a).intersection(set(list_b))
    print(f"Common elements: {common}")
    return


if __name__ == "__main__":
    app.run()
