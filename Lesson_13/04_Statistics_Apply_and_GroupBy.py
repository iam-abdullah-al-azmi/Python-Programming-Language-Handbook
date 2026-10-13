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
    # Statistics, Apply and GroupBy
    Learn how to summarise columns with statistics, transform columns with `apply`, work with dates, and summarise groups of rows with `groupby`.
    """)
    return


@app.cell
def _():
    from pathlib import Path

    import pandas as pd

    folder = Path(__file__).resolve().parent
    df = pd.read_csv(folder / "New_Student_Info.csv", index_col=0)
    df.head()
    return (df, folder, pd)


@app.cell
def _(mo):
    mo.md(r"""
    ## Statistical functions
    Statistics skip missing values by default, so a few students with a missing mark do not break the result.
    """)
    return


@app.cell
def _(df):
    _marks = df["Data Structure Marks"]
    print("sum   :", _marks.sum())
    print("max   :", _marks.max())
    print("min   :", _marks.min())
    print("mean  :", _marks.mean())
    print("median:", _marks.median())
    return


@app.cell
def _(df):
    # mode is the value with the highest frequency (it returns a Series because of possible ties)
    print(df["Data Structure Marks"].mode())
    # standard deviation
    print(df["Data Structure Marks"].std())
    return


@app.cell
def _(df):
    marks_columns = ["Data Structure Marks", "Algorithm Marks", "Python Marks", "Total Marks"]
    print(df[marks_columns].corr())
    return (marks_columns,)


@app.cell
def _(df, marks_columns):
    # sum of the different columns
    print(df[marks_columns].sum())
    # row wise summation
    print(df[["Data Structure Marks", "Algorithm Marks"]].sum(axis=1).head())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Apply
    `apply` runs a function on every value of a column. This is min-max scaling, which maps the smallest total to 0 and the largest to 1, written with a lambda.
    """)
    return


@app.cell
def _(df):
    _mn = df["Total Marks"].min()
    _mx = df["Total Marks"].max()

    df["Scaled Total Marks"] = df["Total Marks"].apply(lambda x: (x - _mn) / (_mx - _mn))
    print(df[["FullName", "Total Marks", "Scaled Total Marks"]].head())
    return


@app.cell
def _(mo):
    mo.md(r"""
    You can also pass your own named function.
    """)
    return


@app.cell
def _(df):
    def grading_system(marks):
        if marks >= 260:
            return "A+"
        elif marks >= 240:
            return "A"
        else:
            return "A-"


    df["Grade"] = df["Total Marks"].apply(grading_system)
    print(df[["FullName", "Total Marks", "Grade"]].head())
    return (grading_system,)


@app.cell
def _(mo):
    mo.md(r"""
    With `axis=1`, `df.apply` calls the function once per row, so the function can use several columns at once.
    """)
    return


@app.cell
def _(df):
    def marking_system(row):
        a = row["Data Structure Marks"] * 2
        b = row["Python Marks"] * 3
        c = row["Algorithm Marks"] * 4

        return a + b + c


    df["Exceptional Marks"] = df.apply(marking_system, axis=1)
    print(df[["FullName", "Exceptional Marks"]].head())
    return (marking_system,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Dates and times
    Dates read from a CSV file are plain text. `pd.to_datetime` converts them, after which the `.dt` accessor gives parts such as the year and month.
    """)
    return


@app.cell
def _(df, pd):
    print(df["EnrollmentDate"].dtype)
    df["EnrollmentDate"] = pd.to_datetime(df["EnrollmentDate"])
    print(df["EnrollmentDate"].dtype)
    print(df["EnrollmentDate"].head())
    return


@app.cell
def _(df):
    df["Enrollment Year"] = df["EnrollmentDate"].dt.year
    df["Enrollment Month"] = df["EnrollmentDate"].dt.month
    print(df[["EnrollmentDate", "Enrollment Year", "Enrollment Month"]].head())
    return


@app.cell
def _(mo):
    mo.md(r"""
    `pd.date_range` makes a sequence of dates. Subtracting two date columns gives a time difference (a timedelta).
    """)
    return


@app.cell
def _(df, pd):
    df["Finished Date"] = pd.date_range("2025-11-01", "2026-12-31", periods=len(df["EnrollmentDate"]))
    df["Time taken to finish"] = df["Finished Date"] - df["EnrollmentDate"]
    print(df[["EnrollmentDate", "Finished Date", "Time taken to finish"]].head())
    return


@app.cell
def _(df):
    print(df.drop(columns=["EnrollmentDate", "Finished Date"]).head())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## GroupBy
    `groupby` splits the rows into groups that share a value, then an aggregation such as `min`, `max` or `mean` is computed for every group.
    """)
    return


@app.cell
def _(df):
    group_by_instructor = df.groupby("Instructor")
    print(group_by_instructor["Total Marks"].min())
    print(group_by_instructor["Total Marks"].max())
    return (group_by_instructor,)


@app.cell
def _(group_by_instructor):
    print(group_by_instructor["Time taken to finish"].min())
    print(group_by_instructor["Time taken to finish"].max())
    return


@app.cell
def _(group_by_instructor):
    # the first and the last row of every group
    print(group_by_instructor[["FullName", "Total Marks"]].first())
    print(group_by_instructor[["FullName", "Total Marks"]].last())
    return


@app.cell
def _(group_by_instructor):
    print(group_by_instructor["Total Marks"].agg(["count", "mean", "max"]))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### GroupBy on a larger dataset
    The IPL 2022 auction dataset has one row per player. Group by team to count the players and find the average cost in crore rupees.
    """)
    return


@app.cell
def _(folder, pd):
    ipl = pd.read_csv(folder / "ipl_2022_dataset.csv", index_col=0)
    ipl = ipl.rename(columns={"COST IN ₹ (CR.)": "Cost Cr"})
    print(ipl.head())
    return (ipl,)


@app.cell
def _(ipl):
    by_team = ipl.groupby("Team")
    print(by_team["Player"].count())
    print(by_team["Cost Cr"].mean().round(2))
    return


if __name__ == "__main__":
    app.run()
