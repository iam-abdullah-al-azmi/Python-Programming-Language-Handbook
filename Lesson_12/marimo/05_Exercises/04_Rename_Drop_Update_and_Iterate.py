import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Pandas Foundations Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 04: On a copy of the DataFrame rename FullName to Full Name, drop the Instructor column and drop row 0. Then set the Python Marks of row 1 to 90, add 2 marks to the Python Marks of rows 1 to 3, and loop over the first five rows with iterrows and itertuples printing each student's name and Python Marks.
    """)
    return


@app.cell(hide_code=True)
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    _copy = df.copy()
    _copy = _copy.rename(columns={"FullName": "Full Name"})
    _copy = _copy.drop("Instructor", axis=1)
    _copy = _copy.drop(0)
    print(_copy.columns.tolist())
    print("Rows before:", len(df), "| after:", len(_copy))

    _copy = df.copy()
    print("Before:\n", _copy.loc[1:3, ["FullName", "Python Marks"]])
    _copy.loc[1, "Python Marks"] = 90
    _copy.loc[1:3, "Python Marks"] += 2
    print("After:\n", _copy.loc[1:3, ["FullName", "Python Marks"]])

    _first = _copy.head(5)
    print("Using iterrows:")
    for _i, _row in _first.iterrows():
        print(f"{_i}: {_row['FullName']} -> {_row['Python Marks']}")
    print("Using itertuples:")
    for _row in _first.itertuples():
        print(f"{_row.Index}: {_row.FullName} -> {_row[5]}")
    return


if __name__ == "__main__":
    app.run()
