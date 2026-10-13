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
    # Inspecting and Selecting Data
    Learn how to look at a DataFrame (head, tail, info, describe) and how to select columns and rows with square brackets, `loc` and `iloc`.
    """)
    return


@app.cell
def _():
    from pathlib import Path

    import numpy as np
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent / "student_data.csv")
    return (df, np)


@app.cell
def _(mo):
    mo.md(r"""
    ## Inspecting a DataFrame
    """)
    return


@app.cell
def _(df):
    print(df.head())
    return


@app.cell
def _(df):
    print(df.tail(3))
    return


@app.cell
def _(df, np):
    # the column names, as an Index, a list and a NumPy array
    print(df.columns)

    columns_list = list(df.columns)
    print(columns_list)

    columns_array = np.array(columns_list)
    print(columns_array, columns_array.dtype)
    return (columns_list, columns_array)


@app.cell
def _(df):
    print(df.index)
    print(df.shape)
    print(df.dtypes)
    return


@app.cell
def _(df):
    # column names, non-null counts and data types
    df.info()
    return


@app.cell
def _(df):
    # random rows; random_state makes the sample repeatable
    print(df.sample(5, random_state=1))
    return


@app.cell
def _(df):
    # count, mean, std, min, quartiles and max of the numeric columns
    print(df.describe())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Selecting columns
    Square brackets with a column name give a Series. A list of names gives a DataFrame.
    """)
    return


@app.cell
def _(df):
    print(type(df["FullName"]))
    print(df["FullName"].head())
    return


@app.cell
def _(df):
    print(type(df[["FullName", "Python Marks"]]))
    print(df[["FullName", "Python Marks"]].head())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Selecting rows and columns with loc
    `loc` selects by label: `df.loc[row_start:row_end, col_start:col_end]`. Unlike normal Python slicing, the end label of a `loc` slice is included.
    """)
    return


@app.cell
def _(df):
    # a single row gives a Series
    print(df.loc[0])
    print(type(df.loc[0]))
    return


@app.cell
def _(df):
    # multiple rows
    print(df.loc[[2, 3, 19]])
    return


@app.cell
def _(df):
    # multiple rows using a range (3 to 7 inclusive)
    print(df.loc[3:7])
    return


@app.cell
def _(df):
    # single column
    print(df.loc[:, ["Python Marks"]].head())
    return


@app.cell
def _(df):
    # multiple columns
    print(df.loc[:, ["Python Marks", "Algorithm Marks"]].head())
    return


@app.cell
def _(df):
    # rows with columns
    print(df.loc[3:7, ["CompletionStatus"]])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Setting an index and selecting with iloc
    `set_index` turns a column into the row labels. `iloc` always selects by integer position (the end of the slice is excluded, as in normal Python), while `loc` uses the labels.
    """)
    return


@app.cell
def _(df):
    indexed = df.set_index("StudentID")
    print(indexed.head(3))
    return (indexed,)


@app.cell
def _(indexed):
    # position 3 up to (but not including) position 7
    print(indexed.iloc[3:7])
    return


@app.cell
def _(indexed):
    print(indexed.loc["PH1003"])
    print(indexed.loc["PH1003", "FullName"])
    return


@app.cell
def _(indexed):
    # loc uses labels, so slicing with numbers on a text index is an error
    try:
        indexed.loc[3:7]
    except TypeError as _error:
        print("TypeError:", _error)
    return


if __name__ == "__main__":
    app.run()
