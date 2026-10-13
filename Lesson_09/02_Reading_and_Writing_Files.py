import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Exceptions, Files and Modules")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Reading and Writing Files
    Learn how to open a text file in Python, read it in different ways, and write or append text using the file modes `r`, `w`, `w+` and `a+`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Reading a file
    `open(path, "r")` opens a file in read mode (the default mode when nothing is mentioned).
    `read()` returns the whole content as one string. The file is `sample.txt`, which lives next to this notebook.
    """)
    return


@app.cell
def _():
    from pathlib import Path

    path = Path(__file__).resolve().parent / "sample.txt"
    _file = open(path, "r")  # file open in read mode only, if we don't mention anything this is the default mode
    _content = _file.read()
    print(_content, type(_content))

    return Path, path


@app.cell
def _(mo):
    mo.md(r"""
    `readlines()` returns a list with one string per line. A file opened by hand must be closed with `close()`.
    """)
    return


@app.cell
def _(path):
    _file = open(path, "r")
    _content = _file.readlines()
    print(_content, type(_content))
    print(_file.closed)
    _file.close()
    print(_file.closed)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## The with statement
    When we use the `with` statement we don't have to worry about closing the file; Python closes it automatically.
    """)
    return


@app.cell
def _(path):
    with open(path, "r") as _file:
        _content = _file.readlines()
        print(_content, type(_content))
    print(_file.closed)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Reading line by line
    A file can be used directly in a `for` loop. Every line already ends with a new line character, so `print` adds a blank line. Use `end=""` or `strip()` to avoid it.
    """)
    return


@app.cell
def _(path):
    with open(path, "r") as _file:
        for _line in _file:
            print(_line)
    return


@app.cell
def _(path):
    with open(path, "r") as _file:
        for _line in _file:
            print(_line, end="")
    return


@app.cell
def _(path):
    with open(path, "r") as _file:
        for _line in _file:
            _stripped = _line.strip()
            print(_stripped)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Writing a file
    The examples below write to a temporary folder so that nothing is left behind next to the notebook.

    - `"w"` opens the file in write mode: if the file already exists it is overwritten.
    - `write()` does not add a new line by itself, so the three lines below end up joined together.
    """)
    return


@app.cell
def _(Path):
    import tempfile

    workspace = tempfile.mkdtemp()
    out_path = Path(workspace) / "test.txt"

    with open(out_path, "w") as _file:
        _file.write("Hello test file line 1.")
        _file.write("Hello test file line 2.")
        _file.write("Hello test file line 3.")

    with open(out_path, "r") as _file:
        print(_file.read(), end="")

    return out_path, workspace


@app.cell
def _(mo):
    mo.md(r"""
    `"w+"` allows writing and reading at the same time. After writing, `seek(0)` moves the cursor back to the start of the file so that we can read from the beginning.
    """)
    return


@app.cell
def _(out_path):
    with open(out_path, "w+") as _file:
        _file.write("Hello test file with write plus read mode line 1.")
        _file.write("Hello test file with write plus read mode line 2.")
        _file.write("Hello test file with write plus read mode line 3.")
        _file.seek(0)
        print(_file.read(), end="")
    return


@app.cell
def _(mo):
    mo.md(r"""
    `"a+"` opens the file in append mode: instead of overwriting the file, new text is added at the end. The `+` also lets us read.
    """)
    return


@app.cell
def _(out_path):
    with open(out_path, "a+") as _file:
        _file.write("Hello test 2 file.")
        _file.write("Hello test 2 file.")
        _file.write("Hello test 2 file.")
        _file.seek(0)
        print(_file.read(), end="")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Putting it together
    Write lines with `\n`, read them back, remove the new line characters with `strip()` (using `map`) and keep only the long lines (using `filter`).
    """)
    return


@app.cell
def _(out_path):
    with open(out_path, "a+") as _file:
        _file.write("\nNew Line ONE\n")
        _file.write("New Line TWO\n")
        _file.write("New Line THREE\n")
        _file.write("New Line FOUR\n")
        _file.seek(0)
        _content = _file.readlines()
        print(f"Content of the file: \n{_content}\n")
        _content = list(map(str.strip, _content))  # removing the new line characters using the strip() function
        print(f"Content of the mapped file for removing new line: \n{_content}\n")
        _filtered_content = list(filter(lambda val: len(val) > 15, _content))
        print(f"Filtered Content of the file for length greater than 15: \n{_filtered_content}")
    return


@app.cell
def _(Path, workspace):
    import shutil

    shutil.rmtree(workspace)  # clean up the temporary folder
    print(Path(workspace).exists())
    return


if __name__ == "__main__":
    app.run()
