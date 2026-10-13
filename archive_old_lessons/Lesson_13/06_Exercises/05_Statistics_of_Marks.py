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
        Exercise 05: Print the sum, max, min, mean, median, mode and standard deviation of Data Structure Marks, plus the correlation matrix of the three marks columns.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    _ds = df["Data Structure Marks"]
    print("Sum   :", _ds.sum())
    print("Max   :", _ds.max())
    print("Min   :", _ds.min())
    print("Mean  :", round(_ds.mean(), 2))
    print("Median:", _ds.median())
    print("Mode  :", _ds.mode().tolist())
    print("Std   :", round(_ds.std(), 2))

    _marks = ["Data Structure Marks", "Algorithm Marks", "Python Marks"]
    print(df[_marks].corr())
    return


if __name__ == "__main__":
    app.run()
