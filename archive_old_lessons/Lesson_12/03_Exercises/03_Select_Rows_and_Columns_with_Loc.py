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
        Exercise 03: Using loc, select row 0, rows 3 to 7, the Python Marks column and the CompletionStatus of rows 3 to 7.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    print("Row 0:\n", df.loc[0])
    print("Rows 3 to 7:\n", df.loc[3:7])
    print("Python Marks:\n", df.loc[:, ["Python Marks"]].head())
    print("CompletionStatus rows 3-7:\n", df.loc[3:7, ["CompletionStatus"]])
    return


if __name__ == "__main__":
    app.run()
