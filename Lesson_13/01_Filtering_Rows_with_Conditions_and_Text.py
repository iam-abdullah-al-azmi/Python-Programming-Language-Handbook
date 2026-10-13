import marimo

__generated_with = "0.24.0"

app = marimo.App(width="medium", app_title="Pandas Data Cleaning and Analysis")


@app.cell
def _():
    import marimo as mo

    return (mo,)

@app.cell
def _(mo):
    mo.md(r"""
    # Filtering Rows with Conditions and Text
    Learn how to keep only the rows you want, using boolean conditions on numbers and the `str.contains` method (with regular expressions) on text.
    """)
    return


@app.cell
def _():
    from pathlib import Path

    import pandas as pd

    students = pd.read_csv(Path(__file__).resolve().parent / "student_data.csv")
    return (pd, students)


@app.cell
def _(mo):
    mo.md(r"""
    ## Filtering with conditions
    A comparison such as `df["Python Marks"] > 85` produces a boolean Series (True or False for every row). Passing it to `loc` keeps only the rows that are True.
    """)
    return


@app.cell
def _(students):
    print((students["Python Marks"] > 85).head())
    print(students.loc[students["Python Marks"] > 85, ["FullName", "Python Marks"]])
    return


@app.cell
def _(mo):
    mo.md(r"""
    Combine conditions with `&` (and), `|` (or) and `~` (not). Every condition must be wrapped in parentheses.
    """)
    return


@app.cell
def _(students):
    print(students.loc[(students["Python Marks"] > 85) & (students["Instructor"] == "Mr. Karim"), ["FullName", "Instructor", "Python Marks"]])
    print(students.loc[(students["Location"] == "Dhaka") | (students["Location"] == "Sylhet"), ["FullName", "Location"]])
    return


@app.cell
def _(students):
    # isin checks membership in a list, between checks a range (both ends included)
    print(students.loc[students["Location"].isin(["Sylhet", "Khulna"]), ["FullName", "Location"]])
    print(students.loc[students["Python Marks"].between(80, 85), ["FullName", "Python Marks"]])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Filtering text with str.contains
    The `.str` accessor applies string methods to every value of a text column. We use a small DataFrame to practise.
    """)
    return


@app.cell
def _(pd):
    _data = {
        "Name": ["Alice one", "Bob two", "Cha one", "Dada two", "Esa One"],
        "City": ["Los abcd RK", "New efgh RK", "Los ijkl RKA", "new mnop RKA", "qrst new los rka"],
        "Department": ["EEE", "MPE", "EEE", "CSE", "SWE"],
        "Salary": [10, 20, 30, 40, 50],
    }

    df = pd.DataFrame(_data)
    df
    print(df)
    return (df,)


@app.cell
def _(df):
    # case sensitive: "One" in "Esa One" does not match
    print(df.loc[df["Name"].str.contains("one")])
    return


@app.cell
def _(df):
    # case=False ignores upper/lower case
    print(df.loc[df["Name"].str.contains("one", case=False)])
    return


@app.cell
def _(df):
    print(df.loc[df["City"].str.contains(r"Los", case=False)])
    return


@app.cell
def _(mo):
    mo.md(r"""
    `str.contains` accepts regular expressions: `^` means "starts with", `$` means "ends with", `[...]` matches any one of the listed characters and `|` means "or".
    """)
    return


@app.cell
def _(df):
    # starts with Los
    print(df.loc[df["City"].str.contains(r"^Los", case=False)])
    return


@app.cell
def _(df):
    print(df.loc[df["City"].str.contains(r"RK", case=False)])
    return


@app.cell
def _(df):
    # ends with RK
    print(df.loc[df["City"].str.contains(r"RK$", case=False)])
    return


@app.cell
def _(df):
    # names that start with a vowel
    print(df.loc[df["Name"].str.contains(r"^[AEIOU]", case=False)])
    return


@app.cell
def _(df):
    # city contains RK or RKA
    print(df.loc[df["City"].str.contains(r"RK|RKA", case=False)])
    return


@app.cell
def _(mo):
    mo.md(r"""
    For simple prefixes and suffixes, `str.startswith` and `str.endswith` do the same job without regular expressions.
    """)
    return


@app.cell
def _(df):
    print(df.loc[df["City"].str.startswith("Los")])
    print(df.loc[df["Name"].str.endswith("two")])
    return


if __name__ == "__main__":
    app.run()
