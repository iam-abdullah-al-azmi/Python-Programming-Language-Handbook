import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Matplotlib Visualization Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 04: Here, you have to draw a pie chart showing the share of total enrollment between Programming and Digital Marketing over all years.
    """)
    return


@app.cell(hide_code=True)
def _():
    import pandas as pd
    from pathlib import Path
    import matplotlib.pyplot as plt

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "enrollment_data.csv")

    totals = [df["Programming"].sum(), df["Digital Marketing"].sum()]

    plt.pie(totals, labels=["Programming", "Digital Marketing"], autopct="%1.1f%%")
    plt.title("Share of Total Enrollment")
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
