import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Matplotlib Visualization")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 02: Here, you have to plot Programming and Digital Marketing enrollment together, using different colors, markers and a legend.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "enrollment_data.csv")

    plt.title("Programming vs Digital Marketing Enrollment")
    plt.xlabel("Year")
    plt.ylabel("Enrollment")
    plt.plot(df["Year"], df["Programming"], label="Programming", color="#32a852", marker="o")
    plt.plot(df["Year"], df["Digital Marketing"], label="Digital Marketing", color="#8b32a8", linestyle="dotted", marker="o")
    plt.legend()
    plt.grid()
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
