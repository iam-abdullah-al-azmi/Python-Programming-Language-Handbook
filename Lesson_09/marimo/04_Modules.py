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
    # Modules
    Learn how to reuse code with modules: import your own Python file and the modules that ship with Python.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## What is a module
    A module is simply a Python file. Anything defined in it (functions, variables) can be used in another file with `import`.
    This notebook uses `something_in_file.py`, which sits next to it and defines a function `greeting` and a dictionary `person`.
    Importing a module runs its code once, which is why the dictionary is printed when the import happens.
    """)
    return


@app.cell
def _():
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))  # make sure Python can find the file next to this notebook

    import something_in_file as info

    info.greeting(" Azmi")

    return (info,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Using the names inside a module
    Use `module.name` to reach anything the module defines. `as` gives the module a shorter alias.
    """)
    return


@app.cell
def _(info):
    print(info.person)
    print(info.person[0])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Standard library modules
    Python comes with many ready-made modules. `import math` loads the whole module, while `from math import sqrt` loads just one name that can then be used without the prefix.
    """)
    return


@app.cell
def _():
    import math
    from math import sqrt

    print(math.pi)
    print(math.ceil(4.2), math.factorial(5))
    print(sqrt(49))
    return


@app.cell
def _(mo):
    mo.md(r"""
    `dir(module)` lists everything a module offers.
    """)
    return


@app.cell
def _():
    import random

    random.seed(1)  # a seed makes the "random" numbers repeatable
    print(random.randint(1, 10))
    print([name for name in dir(random) if not name.startswith("_")][:5])
    return


if __name__ == "__main__":
    app.run()
