import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 07: Read ipl_2022_dataset.csv and use groupby to find the number of players and the average cost in crore rupees for each team.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "ipl_2022_dataset.csv")

    _by_team = df.groupby("Team")
    print("Players per team:\n", _by_team["Player"].count())
    print("Average cost (Cr) per team:\n", _by_team["COST IN ₹ (CR.)"].mean().round(2))
    return


if __name__ == "__main__":
    app.run()
