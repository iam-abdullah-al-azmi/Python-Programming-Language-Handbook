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
        Exercise 07: Loop over the first five rows using iterrows and itertuples and print each student's name and Python Marks.
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import pandas as pd

    df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
    _first = df.head(5)

    print("Using iterrows:")
    for _i, _row in _first.iterrows():
        print(f"{_i}: {_row['FullName']} -> {_row['Python Marks']}")

    print("Using itertuples:")
    for _i, _name, _marks in zip(_first.index, _first["FullName"], _first["Python Marks"]):
        print(f"{_i}: {_name} -> {_marks}")
    for _row in _first.itertuples():
        print(_row.Index, _row.FullName)
    return


if __name__ == "__main__":
    app.run()
