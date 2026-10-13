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
        Exercise 02: Write three lines to a temporary file using the with statement, then read the file back and print its content.
    """)
    return


@app.cell
def _():
    import os
    import tempfile

    _path = os.path.join(tempfile.gettempdir(), "exercise_02_demo.txt")

    with open(_path, "w") as _file:
        _file.write("Line one\n")
        _file.write("Line two\n")
        _file.write("Line three\n")

    with open(_path, "r") as _file:
        print(_file.read(), end="")

    os.remove(_path)
    return


if __name__ == "__main__":
    app.run()
