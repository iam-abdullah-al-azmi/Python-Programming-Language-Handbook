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
        Exercise 06: Here, you have to draw a Seaborn count plot of how many students are in each subject, split by gender.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import seaborn as sns
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "sns_data.csv")

    ax = sns.countplot(data=df, x="subject", hue="gender")
    ax
    return


if __name__ == "__main__":
    app.run()
