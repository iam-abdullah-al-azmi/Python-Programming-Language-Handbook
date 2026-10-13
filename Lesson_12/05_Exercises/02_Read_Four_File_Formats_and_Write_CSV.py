import marimo

__generated_with = "0.24.0"

app = marimo.App(width="medium", app_title="Pandas Foundations")


@app.cell
def _():
    import marimo as mo

    return (mo,)

@app.cell
def _(mo):
    mo.md(r"""
        Exercise 02: Read student_data.csv, data.json, phitron_student_marks.xlsx and students.parquet and print the shape of each. Then write the first three rows of the CSV DataFrame to a CSV file inside a temporary folder (without the index) and read it back.
    """)
    return


@app.cell
def _():
    import tempfile
    from pathlib import Path
    import pandas as pd

    _folder = Path(__file__).resolve().parent.parent

    df = pd.read_csv(_folder / "student_data.csv")
    _frames = {
        "csv": df,
        "json": pd.read_json(_folder / "data.json"),
        "excel": pd.read_excel(_folder / "phitron_student_marks.xlsx"),
        "parquet": pd.read_parquet(_folder / "students.parquet"),
    }
    for _name, _frame in _frames.items():
        print(_name, _frame.shape)

    with tempfile.TemporaryDirectory() as _tmp:
        _path = Path(_tmp) / "first_three.csv"
        df.head(3).to_csv(_path, index=False)
        print(_path.read_text())
        print(pd.read_csv(_path).shape)
    return


if __name__ == "__main__":
    app.run()
