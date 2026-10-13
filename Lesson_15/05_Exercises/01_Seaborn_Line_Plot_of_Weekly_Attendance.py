import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Seaborn and Plotly Visualization")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 01: Here, you have to draw a Seaborn line plot of attendance_rate by week, with a separate line for each gender and no error band.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import seaborn as sns
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "sns_data.csv")

    ax = sns.lineplot(data=df, x="week", y="attendance_rate", hue="gender", errorbar=None)
    ax
    return


if __name__ == "__main__":
    app.run()
