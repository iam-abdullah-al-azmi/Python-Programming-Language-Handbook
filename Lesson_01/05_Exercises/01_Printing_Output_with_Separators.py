import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Basics Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 01: Print the three words Python, is, fun on one line separated by dashes, then print your name and your city on two lines using one print call and an escape character.
    """)
    return


@app.cell
def _():
    print("Python", "is", "fun", sep="-")
    print("Azmi\nDhaka")
    return


if __name__ == "__main__":
    app.run()
