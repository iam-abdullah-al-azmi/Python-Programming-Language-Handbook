import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Pandas Foundations Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 01: Create a Series of three marks and a DataFrame of three students from a dictionary, print their types, then read student_data.csv and print the type of the DataFrame and of its StudentID column, plus head, tail, columns, index and info.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    marks = pd.Series([88, 92, 75], index=["Alif", "Fatima", "Imran"], name="Python Marks")
    students = pd.DataFrame({"Name": ["Alif", "Fatima", "Imran"], "Python Marks": [88, 92, 75]})
    print(type(marks), type(students), students.shape)

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    print(type(df))
    print(type(df["StudentID"]))
    print(df.head())
    print(df.tail())
    print(list(df.columns))
    print(df.index)
    df.info()
    return


if __name__ == "__main__":
    app.run()
