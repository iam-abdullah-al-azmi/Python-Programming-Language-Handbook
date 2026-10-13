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
        Exercise 03: Here, you have to draw a scatter plot of Study_Hour against IQ_Score with a title, axis labels and a grid.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_IQdata.csv")

    plt.title("Relation between Study Hours and IQ Score")
    plt.xlabel("Study Hours")
    plt.ylabel("IQ Score")
    plt.scatter(df["Study_Hour"], df["IQ_Score"])
    plt.grid()
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
