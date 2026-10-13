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
        Exercise 06: Use reduce() with a lambda function to find the product of all numbers in a list, and the largest number in the same list.
    """)
    return


@app.cell
def _():
    from functools import reduce

    numbers = [2, 3, 4, 5]

    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product: {product}")

    largest = reduce(lambda x, y: x if x > y else y, numbers)
    print(f"Largest: {largest}")
    return


if __name__ == "__main__":
    app.run()
