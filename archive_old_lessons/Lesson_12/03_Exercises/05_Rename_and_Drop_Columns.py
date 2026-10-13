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
        Exercise 05: On a copy of the DataFrame rename FullName to Full Name, drop the Instructor column and drop row 0.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    _copy = df.copy()
    _copy = _copy.rename(columns={"FullName": "Full Name"})
    _copy = _copy.drop("Instructor", axis=1)
    _copy = _copy.drop(0)

    print(_copy.columns.tolist())
    print(_copy.head())
    print("Rows before:", len(df), "| after:", len(_copy))
    return


if __name__ == "__main__":
    app.run()
