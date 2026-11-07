import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Conditionals and Loops Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 01: Check whether a year is a leap year. A year is a leap year if it is divisible by 4 but not by 100, or if it is divisible by 400.
    """)
    return


@app.cell(hide_code=True)
def _():
    year = 2100
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

    return (year,)


if __name__ == "__main__":
    app.run()
