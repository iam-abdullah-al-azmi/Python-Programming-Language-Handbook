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
        Exercise 03: Count the missing values in each column, check whether Python Marks has any NaN, and print the unique instructors and the number of unique values per column.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    print("Missing per column:\n", df.isnull().sum())
    print("Python Marks has NaN:", df["Python Marks"].hasnans)
    print("Unique instructors:", df["Instructor"].unique())
    print("Number of unique instructors:", df["Instructor"].nunique())
    print("Unique values per column:\n", df.nunique())
    return


if __name__ == "__main__":
    app.run()
