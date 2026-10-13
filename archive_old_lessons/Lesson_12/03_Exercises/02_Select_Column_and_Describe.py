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
        Exercise 02: Select the FullName column (check that it is a Series) and print the mean and describe() summary of the numeric marks columns.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    _names = df["FullName"]
    print(type(_names))
    print(_names.head())

    _marks = ["Data Structure Marks", "Algorithm Marks", "Python Marks"]
    print(df[_marks].mean())
    print(df[_marks].describe())
    return


if __name__ == "__main__":
    app.run()
