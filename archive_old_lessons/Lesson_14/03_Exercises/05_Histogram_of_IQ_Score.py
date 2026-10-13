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
        Exercise 05: Here, you have to draw a histogram of IQ_Score with 10 bins and a white edge color.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_IQdata.csv")

    plt.title("Frequency of IQ Score among Students")
    plt.xlabel("IQ Score")
    plt.ylabel("Frequency")
    plt.hist(df["IQ_Score"], bins=10, edgecolor="white")
    plt.grid()
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
