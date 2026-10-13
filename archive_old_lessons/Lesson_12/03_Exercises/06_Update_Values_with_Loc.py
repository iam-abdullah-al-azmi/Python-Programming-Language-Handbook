import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 06: On a copy of the DataFrame, set the Python Marks of row 1 to 90 and add 2 marks to the Python Marks of rows 1 to 3.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    _copy = df.copy()
    print("Before:\n", _copy.loc[1:3, ["FullName", "Python Marks"]])

    _copy.loc[1, "Python Marks"] = 90
    _copy.loc[1:3, "Python Marks"] += 2
    print("After:\n", _copy.loc[1:3, ["FullName", "Python Marks"]])
    return


if __name__ == "__main__":
    app.run()
