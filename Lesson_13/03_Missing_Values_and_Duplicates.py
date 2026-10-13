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
    # Missing Values and Duplicates
    Learn how to find missing values and unique values, and how to remove or fill missing data and remove duplicate rows.
    """)
    return


@app.cell
def _():
    from pathlib import Path

    import pandas as pd

    folder = Path(__file__).resolve().parent
    df = pd.read_csv(folder / "student_data.csv")
    df.head()
    return (df, folder, pd)


@app.cell
def _(mo):
    mo.md(r"""
    ## Finding missing values
    Missing values are stored as NaN. `isnull` marks them with True, `notnull` is the opposite and `hasnans` tells whether a Series has any.
    """)
    return


@app.cell
def _(df):
    print(df["Data Structure Marks"].isnull().head(8))
    return


@app.cell
def _(df):
    print(df["Data Structure Marks"].notnull().head(8))
    return


@app.cell
def _(df):
    print(df["Data Structure Marks"].hasnans)
    print(df["StudentID"].hasnans)
    return


@app.cell
def _(df):
    # isnull on the whole DataFrame, then count the True values per column
    print(df.isnull().head())
    print(df.isnull().sum())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Unique values
    `unique()` only works on a Series, not on a whole DataFrame. It includes NaN as a value, while `nunique()` ignores it.
    """)
    return


@app.cell
def _(df):
    print(df["Instructor"].unique())
    print(len(df["Instructor"].unique()))
    return


@app.cell
def _(df):
    print(df["Algorithm Marks"].unique())
    print(len(df["Algorithm Marks"].unique()))
    return


@app.cell
def _(df):
    # without the null value
    print(df["Algorithm Marks"].nunique())
    print(df.nunique())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Dropping missing values
    `dropna` removes rows that contain a missing value. `how="all"` removes only rows where every value is missing, and `subset` limits the check to the chosen columns.
    """)
    return


@app.cell
def _(df):
    print(len(df), "rows before,", len(df.dropna()), "after dropna()")
    return


@app.cell
def _(df):
    # only rows that are missing every value are removed
    print(len(df.dropna(how="all")))
    return


@app.cell
def _(df):
    # removing rows with a null in the Python Marks column
    print(len(df.dropna(subset=["Python Marks"])))
    return


@app.cell
def _(df):
    # removing rows with a null in multiple columns
    print(len(df.dropna(subset=["Python Marks", "Data Structure Marks"])))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Filling missing values
    `fillna` replaces missing values with a constant or with a calculated value such as the column mean.
    """)
    return


@app.cell
def _(df):
    print(df.fillna(0).head(8))
    return


@app.cell
def _(df):
    print(df["FullName"].fillna("unknown").head())
    return


@app.cell
def _(df):
    print(df["Python Marks"].fillna(df["Python Marks"].mean().round(2)).head(8))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Duplicates
    `duplicated` marks every row that repeats an earlier row. This file (`New_Student_Info.csv`) was saved from the previous notebook, with the row index stored in the first column.
    """)
    return


@app.cell
def _(folder, pd):
    students = pd.read_csv(folder / "New_Student_Info.csv", index_col=0)
    students.head()
    return (students,)


@app.cell
def _(students):
    print(students.duplicated().sum())
    print(students.drop_duplicates().shape)
    return


@app.cell
def _(mo):
    mo.md(r"""
    No complete row repeats here, so we add copies of two rows on purpose and try again.
    """)
    return


@app.cell
def _(pd, students):
    with_copies = pd.concat([students, students.iloc[[0, 1]]], ignore_index=True)
    print(with_copies.shape)
    print(with_copies.duplicated().sum())
    print(with_copies.drop_duplicates().shape)
    return (with_copies,)


@app.cell
def _(mo):
    mo.md(r"""
    `drop_duplicates` returns a new DataFrame. Use `inplace=True` to change the original instead. The `subset` argument compares only some columns and `keep` chooses which copy survives (`"first"`, `"last"` or `False` to drop all copies).
    """)
    return


@app.cell
def _(students):
    # keeps the first student of each completion status
    print(students.drop_duplicates(subset=["CompletionStatus"])[["FullName", "CompletionStatus"]])
    return


@app.cell
def _(students):
    print(students.drop_duplicates(subset=["Country"])[["FullName", "Country"]])
    return


@app.cell
def _(students):
    # keep the last student of each completion status
    print(students.drop_duplicates(subset=["CompletionStatus"], keep="last")[["FullName", "CompletionStatus"]])
    return


if __name__ == "__main__":
    app.run()
