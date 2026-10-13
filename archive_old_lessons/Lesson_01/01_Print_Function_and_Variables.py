import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Print Function and Variables")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    In this module, we will use the print function to compile our first text output!
    """)
    return


@app.cell
def _():
    print("Hello World!")
    print("I'm learning Python!")
    print("Python is a versatile language!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    Now, if we want to print the same text in the previous cell, but side by side, then, we can use the following notation at the end!
    """)
    return


@app.cell
def _():
    print("Hello World!", end=" ")
    print("I'm learning Python.", end=" ")
    print("Python is a versatile language.", end=" ")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    Variable Decleration
    """)
    return


@app.cell
def _():
    a = 30
    b = 20

    a, b
    return


if __name__ == "__main__":
    app.run()
