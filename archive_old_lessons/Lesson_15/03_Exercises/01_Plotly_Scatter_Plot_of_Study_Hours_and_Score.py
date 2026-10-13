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
        Exercise 01: Here, you have to draw a Plotly scatter plot of study_hours against test_score, colored by gender.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import plotly.express as px
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "sns_data.csv")

    fig = px.scatter(data_frame=df, x="study_hours", y="test_score", color="gender")
    fig
    return


if __name__ == "__main__":
    app.run()
