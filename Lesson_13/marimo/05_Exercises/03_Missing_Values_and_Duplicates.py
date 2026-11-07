import marimo

__generated_with = "0.24.0"
app = marimo.App(
    width="medium", app_title="Pandas Data Cleaning and Analysis Exercises"
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 03: Count the missing values in each column, check whether Python Marks has any NaN, print the unique instructors and the number of unique values per column. Then count duplicate rows, keep only the first student of each CompletionStatus with drop_duplicates, drop rows where Python Marks is missing and fill the missing Python Marks with the column mean.
    """)
    return


@app.cell(hide_code=True)
def _():
    import pandas as pd
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    print("Missing per column:\n", df.isnull().sum())
    print("Python Marks has NaN:", df["Python Marks"].hasnans)
    print("Unique instructors:", df["Instructor"].unique())
    print("Number of unique instructors:", df["Instructor"].nunique())
    print("Unique values per column:\n", df.nunique())

    print("Duplicate rows:", df.duplicated().sum())
    print(
        "One student per status:\n",
        df.drop_duplicates(subset=["CompletionStatus"])[
            ["FullName", "CompletionStatus"]
        ],
    )

    print("Rows after dropna on Python Marks:", len(df.dropna(subset=["Python Marks"])))

    _mean = df["Python Marks"].mean().round(2)
    print("Mean used for filling:", _mean)
    print(df["Python Marks"].fillna(_mean).head())
    return


if __name__ == "__main__":
    app.run()
