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
        Excercise 09: Here, you have to uppercase the string.
    """)
    return


@app.cell
def _():
    str = "hello world"
    print(str.upper())
    return


if __name__ == "__main__":
    app.run()
