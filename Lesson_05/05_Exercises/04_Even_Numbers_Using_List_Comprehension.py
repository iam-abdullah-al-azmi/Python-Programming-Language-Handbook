import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Strings and Lists Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 04: Create a list of the squares of all even numbers from 1 to 20 using list comprehension.
    """)
    return


@app.cell
def _():
    squares = [x**2 for x in range(1, 21) if x % 2 == 0]
    print(f"Squares of even numbers: {squares}")

    return


if __name__ == "__main__":
    app.run()
