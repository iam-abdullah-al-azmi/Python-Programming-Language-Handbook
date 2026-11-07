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
    # Series and DataFrame Basics
    Learn the two core pandas data structures: the Series (a single labelled column of data) and the DataFrame (a table made of several Series).
    """)
    return


@app.cell
def _():
    from pathlib import Path

    import pandas as pd
    return (Path, pd)


@app.cell
def _(mo):
    mo.md(r"""
    ## Series
    A Series is a one-dimensional labelled array. By default the labels (the index) are 0, 1, 2, ...
    """)
    return


@app.cell
def _(pd):
    marks = pd.Series([88, 92, 75], name="Python Marks")
    print(marks)
    print(type(marks))
    return (marks,)


@app.cell
def _(marks):
    # a Series has values, an index and a dtype
    print(marks.values)
    print(marks.index)
    print(marks.dtype)
    return


@app.cell
def _(mo):
    mo.md(r"""
    You can choose your own index labels, or build a Series from a dictionary (keys become the labels).
    """)
    return


@app.cell
def _(pd):
    named = pd.Series([88, 92, 75], index=["Alif", "Fatima", "Imran"], name="Python Marks")
    print(named)
    print(named["Fatima"])
    print(named.mean())
    return (named,)


@app.cell
def _(pd):
    from_dict = pd.Series({"Alif": 88, "Fatima": 92, "Imran": 75})
    print(from_dict)
    return (from_dict,)


@app.cell
def _(mo):
    mo.md(r"""
    ## DataFrame
    A DataFrame is tabular data. The simplest way to create one is from a dictionary where every key is a column name and every value is a list of the column's data.
    """)
    return


@app.cell
def _(pd):
    students = pd.DataFrame(
        {
            "Name": ["Alif", "Fatima", "Imran"],
            "Python Marks": [88, 92, 75],
            "City": ["Dhaka", "Chattogram", "Sylhet"],
        }
    )
    print(type(students))
    print(students)
    return (students,)


@app.cell
def _(students):
    # shape is (number of rows, number of columns)
    print(students.shape)
    print(students.columns)
    print(students.dtypes)
    return


@app.cell
def _(mo):
    mo.md(r"""
    A DataFrame can also be built from a list of dictionaries, one dictionary per row.
    """)
    return


@app.cell
def _(pd):
    rows = pd.DataFrame(
        [
            {"Name": "Alif", "Python Marks": 88},
            {"Name": "Fatima", "Python Marks": 92},
        ]
    )
    print(rows)
    return (rows,)


@app.cell
def _(mo):
    mo.md(r"""
    ## DataFrame versus Series
    DataFrame is tabular data and Series is a single row or a single column of it. Selecting one column with square brackets gives a Series.
    """)
    return


@app.cell
def _(students):
    print(type(students["Python Marks"]))
    print(students["Python Marks"])
    return


@app.cell
def _(mo):
    mo.md(r"""
    The same is true for a DataFrame loaded from a file.
    """)
    return


@app.cell
def _(Path, pd):
    df = pd.read_csv(Path(__file__).resolve().parent / "student_data.csv")
    print(type(df))
    print(type(df["StudentID"]))
    df.head()
    return (df,)


if __name__ == "__main__":
    app.run()
