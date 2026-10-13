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
        Exercise 06: Create a small module file in a temporary folder with a function, import it, and call the function. Delete the temporary files afterwards.
    """)
    return


@app.cell
def _():
    import importlib
    import os
    import shutil
    import sys
    import tempfile

    _folder = tempfile.mkdtemp()
    with open(os.path.join(_folder, "exercise_06_helper.py"), "w") as _file:
        _file.write("def square(n):\n")
        _file.write("    return n * n\n")

    sys.path.insert(0, _folder)
    helper = importlib.import_module("exercise_06_helper")
    print(helper.square(7))

    sys.path.remove(_folder)
    sys.modules.pop("exercise_06_helper", None)
    shutil.rmtree(_folder)
    return


if __name__ == "__main__":
    app.run()
