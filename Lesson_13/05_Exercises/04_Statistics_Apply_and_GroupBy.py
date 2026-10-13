import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Pandas Data Cleaning and Analysis Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 04: Print the sum, max, min, mean, median, mode and standard deviation of Data Structure Marks and the correlation matrix of the three marks columns. Create a Total Marks column, give each student a grade with apply and a custom function, extract the enrollment year with to_datetime, and finally read ipl_2022_dataset.csv and use groupby to find the number of players and the average cost in crore rupees for each team.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    _folder = Path(__file__).resolve().parent.parent
    df = pd.read_csv(_folder / "student_data.csv")
    _ds = df["Data Structure Marks"]
    print("Sum   :", _ds.sum())
    print("Max   :", _ds.max())
    print("Min   :", _ds.min())
    print("Mean  :", round(_ds.mean(), 2))
    print("Median:", _ds.median())
    print("Mode  :", _ds.mode().tolist())
    print("Std   :", round(_ds.std(), 2))

    _marks = ["Data Structure Marks", "Algorithm Marks", "Python Marks"]
    print(df[_marks].corr())


    def grade(marks):
        if marks >= 260:
            return "A"
        elif marks >= 240:
            return "B"
        else:
            return "C"


    df["Total Marks"] = df[_marks].sum(axis=1)
    df["Grade"] = df["Total Marks"].apply(grade)
    df["EnrollmentDate"] = pd.to_datetime(df["EnrollmentDate"])
    df["Year"] = df["EnrollmentDate"].dt.year
    print(df[["FullName", "Total Marks", "Grade", "Year"]].head(10))

    ipl = pd.read_csv(_folder / "ipl_2022_dataset.csv")
    _by_team = ipl.groupby("Team")
    print("Players per team:\n", _by_team["Player"].count())
    print("Average cost (Cr) per team:\n", _by_team["COST IN ₹ (CR.)"].mean().round(2))
    return


if __name__ == "__main__":
    app.run()
