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
        Exercise 03: Here, you have to draw a Seaborn regression plot of study_hours against test_score.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import seaborn as sns
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "sns_data.csv")

    ax = sns.regplot(data=df, x="study_hours", y="test_score")
    ax
    return


if __name__ == "__main__":
    app.run()
