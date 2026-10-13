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
        Exercise 03: Write a function using *args that returns the sum of any number of values passed to it.
    """)
    return


@app.cell
def _():
    def add_all(*args):
        total = 0
        for value in args:
            total += value
        return total

    print(add_all(1, 2, 3))
    print(add_all(10, 20, 30, 40, 50))
    return


if __name__ == "__main__":
    app.run()
