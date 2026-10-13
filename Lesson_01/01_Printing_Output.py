import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Basics")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Printing Output
    In this notebook you will use the print function to display text and values, and control how the output looks with the end and sep options and escape characters.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your first output
    The print function displays whatever you give it. Text must be written inside quotes. Each print call writes its output on a new line.
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
    mo.md(r"""
    ## Printing on the same line
    If we want to print the same text as in the previous cell, but side by side, we can use the `end` argument. By default `end` is a new line; here we replace it with a space.
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
    mo.md(r"""
    ## Printing several values
    We can give print many values separated by commas. By default print puts a single space between them. The `sep` argument changes that separator.
    """)
    return


@app.cell
def _():
    print("Python", 3, "is", 2.5, True)
    print("2026", "01", "15", sep="-")
    print("Hello", "World", sep="")
    print("a", "b", "c", sep=" | ", end="!\n")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Escape characters
    A backslash inside a string starts an escape sequence.

    - `\n` ---> new line
    - `\t` ---> tab
    - `\\` ---> a backslash
    - `\"` and `\'` ---> a quote inside a string
    """)
    return


@app.cell
def _():
    print("Line one\nLine two")
    print("Name:\tAzmi")
    print("A backslash looks like this: \\")
    print("She said \"hello\"")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Printing results of expressions
    print can also display the result of a calculation. Text and numbers can be mixed using commas.
    """)
    return


@app.cell
def _():
    print(10 + 5)
    print("10 + 5 =", 10 + 5)
    print("Python " * 3)
    print()
    print("The empty print above gave a blank line.")
    return


if __name__ == "__main__":
    app.run()
