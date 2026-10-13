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
        Exercise 01: Here, you have to draw a line plot of Programming enrollment against Year, with a title, axis labels and a grid.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "enrollment_data.csv")

    plt.title("Programming Enrollment by Year")
    plt.xlabel("Year")
    plt.ylabel("Enrollment")
    plt.plot(df["Year"], df["Programming"])
    plt.grid()
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
