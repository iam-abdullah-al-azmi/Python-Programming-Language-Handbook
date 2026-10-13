import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="NumPy Foundations Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 01: Multiply a Python list and a NumPy array by 3 and explain the difference in the output.
    """)
    return


@app.cell
def _():
    import numpy as np

    _lst = [1, 2, 3]
    _arr = np.array(_lst)

    print(f"List * 3  : {_lst * 3}  (the list is repeated)")
    print(f"Array * 3 : {_arr * 3}  (every element is multiplied)")
    return


if __name__ == "__main__":
    app.run()
