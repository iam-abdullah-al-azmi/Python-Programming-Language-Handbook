import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Functional Tools and Generators")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 02: Use map() with a lambda function to square every number in a list, then use filter() with a lambda function to keep only the squares greater than 20.
    """)
    return


@app.cell
def _():
    numbers = [1, 2, 3, 4, 5, 6]

    squares = list(map(lambda value: value**2, numbers))
    print(squares)

    large_squares = list(filter(lambda value: value > 20, squares))
    print(large_squares)

    return


if __name__ == "__main__":
    app.run()
