import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Fundamental")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 06: Here, you have to draw a bar chart comparing the 2024 enrollment of Programming and Digital Marketing.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "enrollment_data.csv")

    latest = df[df["Year"] == 2024]
    courses = ["Programming", "Digital Marketing"]
    values = [latest["Programming"].iloc[0], latest["Digital Marketing"].iloc[0]]

    plt.title("Enrollment in 2024")
    plt.xlabel("Course")
    plt.ylabel("Enrollment")
    plt.bar(courses, values)
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
