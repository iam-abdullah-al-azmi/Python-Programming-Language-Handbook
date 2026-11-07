import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Basics Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 02: Here, you have to take an input from the user and convert it to an integer.
    """)
    return


@app.cell(hide_code=True)
def _():
    val = input("Enter a number: ")
    print(f"Value before conversion: {val} | Type: {type(val)}")
    val = int(val)
    print(f"Value after conversion: {val} | Type: {type(val)}")
    return


if __name__ == "__main__":
    app.run()
