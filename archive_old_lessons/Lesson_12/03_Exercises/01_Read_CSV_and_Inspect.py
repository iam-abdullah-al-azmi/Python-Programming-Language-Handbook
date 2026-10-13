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
        Exercise 01: Read student_data.csv into a DataFrame and print its type, head, tail, columns, index and info.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    print(type(df))
    print(df.head())
    print(df.tail())
    print(list(df.columns))
    print(df.index)
    df.info()
    return


if __name__ == "__main__":
    app.run()
