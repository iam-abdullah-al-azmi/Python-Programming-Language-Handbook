import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Fundamental")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
        Excercise 01: Swap the values of a, b, and c.
    """)


@app.cell
def _():
    a, b, c = (5, 10, 15)
    a, b, c = (c, a, b)
    print(a, b, c)
    return


if __name__ == "__main__":
    app.run()
