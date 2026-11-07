import marimo

__generated_with = "0.24.0"

app = marimo.App(width="medium", app_title="Pandas Data Cleaning and Analysis")


@app.cell
def _():
    import marimo as mo

    return (mo,)

@app.cell
def _(mo):
    mo.md(r"""
    # Adding and Deriving Columns
    Learn how to create new columns from a constant, from arithmetic on other columns, from conditions with `np.where`, and by splitting text.
    """)
    return


@app.cell
def _():
    import tempfile
    from pathlib import Path

    import numpy as np
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent / "student_data.csv")
    df.head()
    return (Path, df, np, pd, tempfile)


@app.cell
def _(mo):
    mo.md(r"""
    ## Adding a column
    Assigning to a new column name creates it. A single value is repeated for every row.
    """)
    return


@app.cell
def _(df):
    df["Country"] = "Bangladesh"
    print(df[["FullName", "Country"]].head())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Column arithmetic
    Arithmetic between columns is done element by element. A missing value (NaN) in any term makes the result NaN.
    """)
    return


@app.cell
def _(df):
    df["Total Marks"] = df["Algorithm Marks"] + df["Python Marks"] + df["Data Structure Marks"]
    print(df[["FullName", "Total Marks"]].head())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Conditional columns with np.where
    `np.where(condition, value_if_true, value_if_false)` builds a column from a condition.
    """)
    return


@app.cell
def _(df, np):
    df["A+ in DS"] = np.where(df["Data Structure Marks"] > 90, "A+", "A")
    print(df[["FullName", "Data Structure Marks", "A+ in DS"]].head())
    return


@app.cell
def _(df, np):
    df["Passed in DS"] = np.where(df["Data Structure Marks"] > 70, "Passed", "Failed")
    print(df[["FullName", "Data Structure Marks", "Passed in DS"]].head())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Splitting text into columns
    `str.split` splits every value; `.str[0]` then picks the first piece, `.str[1]` the second.
    """)
    return


@app.cell
def _(df):
    df["First Name"] = df["FullName"].str.split(" ").str[0]
    df["Last Name"] = df["FullName"].str.split(" ").str[1]
    print(df[["FullName", "First Name", "Last Name"]].head())
    return


@app.cell
def _(df):
    df
    print(df.shape)
    print(df.columns.tolist())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Saving the result
    `to_csv` writes the DataFrame to a file. To keep the repository clean the file is written to a temporary folder, read back, and deleted again.
    """)
    return


@app.cell
def _(Path, df, pd, tempfile):
    with tempfile.TemporaryDirectory() as _tmp:
        _filepath = Path(_tmp) / "New_Student_Info.csv"
        df.to_csv(_filepath)
        print(_filepath.name, "written with", len(_filepath.read_text().splitlines()), "lines")
        print(pd.read_csv(_filepath).columns.tolist())
    return


@app.cell
def _(mo):
    mo.md(r"""
    Notice the extra first column named `Unnamed: 0` when the file is read back: it is the old row index that `to_csv` saved. Use `df.to_csv(path, index=False)` to leave it out, or read with `index_col=0` to restore it as the index.
    """)
    return


if __name__ == "__main__":
    app.run()
