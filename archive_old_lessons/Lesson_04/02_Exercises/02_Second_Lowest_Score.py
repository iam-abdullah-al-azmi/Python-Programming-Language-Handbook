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
        Exercise 02: From a nested list of [name, score] pairs, print the names of the students with the second lowest score in alphabetical order.
    """)
    return


@app.cell
def _():
    students = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41.0], ["Harsh", 39.0]]
    second_lowest = sorted({score for _, score in students})[1]
    names = sorted([name for name, score in students if score == second_lowest])
    print(f"Second lowest score: {second_lowest}")
    for name in names:
        print(name)
    return


if __name__ == "__main__":
    app.run()
