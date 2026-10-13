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
        Exercise 04: Set StudentID as the index, then select the rows at positions 3 to 6 with iloc and the row labelled PH1003 with loc.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    _indexed = df.set_index("StudentID")

    print("iloc[3:7]:\n", _indexed.iloc[3:7])
    print("loc PH1003:\n", _indexed.loc["PH1003"])
    return


if __name__ == "__main__":
    app.run()
