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
    # Modifying and Iterating Over Data
    Learn how to rename and drop columns and rows, update values with `loc`, and loop over the rows of a DataFrame.
    """)
    return


@app.cell
def _():
    from pathlib import Path

    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent / "student_data.csv")
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Renaming columns
    Most DataFrame methods return a new DataFrame and leave the original untouched. Passing `inplace=True` modifies the original object instead of making a copy (and returns `None`).
    """)
    return


@app.cell
def _(df):
    renamed = df.rename(
        columns={
            "FullName": "Full Name",
            "CompletionStatus": "Completion Status",
            "EnrollmentDate": "Enrollment Date",
        }
    )
    print(renamed.columns.tolist())
    print(df.columns.tolist())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Dropping rows and columns
    `drop` removes rows by default; pass `axis=1` (or `columns=`) to remove columns.
    """)
    return


@app.cell
def _(df):
    # row deletion
    print(df.drop(0).head(3))
    return


@app.cell
def _(df):
    # column deletion
    print(df.drop("Instructor", axis=1).columns.tolist())
    return


@app.cell
def _(df):
    # the original DataFrame is unchanged
    print(df.shape)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Updating values
    `loc` can also assign: `df.loc[row, column] = value`. Compound operators such as `+=` work on a whole slice.
    """)
    return


@app.cell
def _(df):
    df.loc[1, "Python Marks"] = 90
    df.loc[1, "CompletionStatus"] = "Completed"
    print(df.loc[0:3, ["FullName", "Python Marks", "CompletionStatus"]])
    return


@app.cell
def _(df):
    df.loc[1:3, "Python Marks"] += 2
    print(df.loc[0:3, ["FullName", "Python Marks"]])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Iterating over rows
    `iterrows` yields an (index, Series) pair for each row. `itertuples` yields a named tuple per row and is faster.
    """)
    return


@app.cell
def _(df):
    for _i, _row in df.head(3).iterrows():
        print(f"{_i}: {_row['FullName']} -> {_row['Python Marks']}")
    return


@app.cell
def _(df):
    for _row in df.head(3).itertuples():
        print(_row)
    return


@app.cell
def _(df):
    for _row in df.head(3).itertuples():
        print(_row.Index, _row.FullName, _row.Location)
    return


if __name__ == "__main__":
    app.run()
