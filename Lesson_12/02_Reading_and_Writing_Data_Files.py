import marimo

__generated_with = "0.24.0"

app = marimo.App(width="medium", app_title="Pandas Foundations")


@app.cell
def _():
    import marimo as mo

    return (mo,)

@app.cell
def _(mo):
    mo.md(r"""
    # Reading and Writing Data Files
    Learn how to load data from CSV, JSON, Excel and Parquet files into a DataFrame, and how to write a DataFrame back out to those formats.
    """)
    return


@app.cell
def _():
    import tempfile
    from pathlib import Path

    import pandas as pd

    folder = Path(__file__).resolve().parent
    return (Path, folder, pd, tempfile)


@app.cell
def _(mo):
    mo.md(r"""
    ## Reading files
    Each file format has its own `read_*` function. They all return a DataFrame. Start with a CSV (comma separated values) file.
    """)
    return


@app.cell
def _(folder, pd):
    df = pd.read_csv(folder / "student_data.csv")
    df.head()
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""
    `read_csv` has many optional arguments: `usecols` picks columns, `nrows` reads only the first rows and `index_col` chooses the column used as the index.
    """)
    return


@app.cell
def _(folder, pd):
    print(pd.read_csv(folder / "student_data.csv", usecols=["StudentID", "FullName"], nrows=3))
    print(pd.read_csv(folder / "student_data.csv", index_col="StudentID").head(3))
    return


@app.cell
def _(mo):
    mo.md(r"""
    JSON, Excel and Parquet files are read in the same way.
    """)
    return


@app.cell
def _(folder, pd):
    json_df = pd.read_json(folder / "data.json")
    json_df
    return (json_df,)


@app.cell
def _(folder, pd):
    excel_df = pd.read_excel(folder / "phitron_student_marks.xlsx")
    excel_df.head()
    return (excel_df,)


@app.cell
def _(folder, pd):
    parquet_df = pd.read_parquet(folder / "students.parquet")
    parquet_df.head()
    return (parquet_df,)


@app.cell
def _(df, excel_df, json_df, parquet_df):
    for _name, _frame in [("csv", df), ("json", json_df), ("excel", excel_df), ("parquet", parquet_df)]:
        print(_name, _frame.shape)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Writing files
    `to_csv`, `to_json`, `to_excel` and `to_parquet` save a DataFrame. Here the files are written to a temporary folder that is deleted automatically, so nothing is left behind. Pass `index=False` to avoid saving the row index as an extra column.
    """)
    return


@app.cell
def _(Path, df, pd, tempfile):
    _small = df[["StudentID", "FullName", "Python Marks"]].head(3)

    with tempfile.TemporaryDirectory() as _tmp:
        _out = Path(_tmp)

        _small.to_csv(_out / "small.csv", index=False)
        _small.to_json(_out / "small.json", orient="records", indent=2)
        _small.to_excel(_out / "small.xlsx", index=False)
        _small.to_parquet(_out / "small.parquet")

        print(sorted(_p.name for _p in _out.iterdir()))
        print((_out / "small.csv").read_text())
        print((_out / "small.json").read_text())

        print(pd.read_csv(_out / "small.csv"))
        print(pd.read_parquet(_out / "small.parquet"))
    return


if __name__ == "__main__":
    app.run()
