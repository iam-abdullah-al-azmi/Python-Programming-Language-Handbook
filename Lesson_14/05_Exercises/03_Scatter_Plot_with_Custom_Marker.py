import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Matplotlib Visualization Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 03: Here, you have to draw a scatter plot of Chilling_Hours against IQ_Score using the x marker.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_IQdata.csv")

    plt.title("Relation between Chilling Hours and IQ Score")
    plt.xlabel("Chilling Hours")
    plt.ylabel("IQ Score")
    plt.scatter(df["Chilling_Hours"], df["IQ_Score"], marker="x")
    plt.grid()
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
