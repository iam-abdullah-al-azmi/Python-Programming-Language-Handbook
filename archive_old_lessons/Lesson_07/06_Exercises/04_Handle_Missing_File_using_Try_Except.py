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
        Exercise 04: Try to open a file that does not exist and handle the FileNotFoundError with a try-except block. Print a message in the else and finally blocks too.
    """)
    return


@app.cell
def _():
    import os
    import tempfile

    _missing_path = os.path.join(tempfile.gettempdir(), "this_file_does_not_exist_12345.txt")

    try:
        with open(_missing_path, "r") as _file:
            _content = _file.read()
    except FileNotFoundError:
        print("File not found!")
    else:
        print(f"Content: {_content}")
    finally:
        print("Execution is complete")
    return


if __name__ == "__main__":
    app.run()
