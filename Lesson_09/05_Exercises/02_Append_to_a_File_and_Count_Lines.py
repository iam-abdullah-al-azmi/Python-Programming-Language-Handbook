import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Exceptions, Files and Modules Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 02: Create a temporary file, append two more lines to it, then read it line by line and count the total number of lines. Also try to open a file that does not exist and handle the FileNotFoundError.
    """)
    return


@app.cell
def _():
    import os
    import tempfile

    _path = os.path.join(tempfile.gettempdir(), "exercise_02_demo.txt")

    with open(_path, "w") as _file:
        _file.write("apple\n")
        _file.write("banana\n")

    with open(_path, "a") as _file:
        _file.write("cherry\n")
        _file.write("date\n")

    _count = 0
    with open(_path, "r") as _file:
        for _line in _file:
            _count += 1
            print(_line.strip())

    print(f"Total lines: {_count}")
    os.remove(_path)

    try:
        with open(_path, "r") as _file:
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
