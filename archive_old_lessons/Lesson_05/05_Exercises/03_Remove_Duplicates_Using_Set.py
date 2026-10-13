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
        Exercise 03: Remove the duplicate values from a list using a set and print the sorted unique values.
    """)
    return


@app.cell
def _():
    numbers = [3, 1, 2, 3, 4, 1, 5, 2, 5]
    unique = set(numbers)
    print(f"Original list: {numbers}")
    print(f"Unique values: {sorted(unique)}")
    return


if __name__ == "__main__":
    app.run()
