import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Tuples, Sets and Dictionaries")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 01: Swap the values of a, b and c by rotating them with tuple unpacking, then count how many times a value appears in a tuple and find the index of its first occurrence.
    """)
    return


@app.cell
def _():
    a, b, c = (5, 10, 15)
    a, b, c = (c, a, b)
    print(a, b, c)
    return


@app.cell
def _():
    tup = (10, 20, 10, 30, 10, 40)
    print(f"Tuple: {tup}")
    print(f"Count of 10: {tup.count(10)}")
    print(f"First index of 30: {tup.index(30)}")
    return


if __name__ == "__main__":
    app.run()
