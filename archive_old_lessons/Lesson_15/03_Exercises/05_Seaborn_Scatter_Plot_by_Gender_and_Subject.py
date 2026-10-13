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
        Exercise 05: Here, you have to draw a Seaborn scatter plot of study_hours against test_score with hue set to gender and style set to subject.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import seaborn as sns
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "sns_data.csv")

    ax = sns.scatterplot(data=df, x="study_hours", y="test_score", hue="gender", style="subject")
    ax
    return


if __name__ == "__main__":
    app.run()
