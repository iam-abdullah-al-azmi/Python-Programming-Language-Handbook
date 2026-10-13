import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 06: Create a Total Marks column, give each student a grade with apply and a custom function, convert EnrollmentDate with to_datetime and extract the year and month.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    def grade(marks):
        if marks >= 260:
            return "A"
        elif marks >= 240:
            return "B"
        else:
            return "C"


    df["Total Marks"] = df["Data Structure Marks"] + df["Algorithm Marks"] + df["Python Marks"]
    df["Grade"] = df["Total Marks"].apply(grade)

    df["EnrollmentDate"] = pd.to_datetime(df["EnrollmentDate"])
    df["Year"] = df["EnrollmentDate"].dt.year
    df["Month"] = df["EnrollmentDate"].dt.month

    print(df[["FullName", "Total Marks", "Grade", "Year", "Month"]].head(10))
    return


if __name__ == "__main__":
    app.run()
