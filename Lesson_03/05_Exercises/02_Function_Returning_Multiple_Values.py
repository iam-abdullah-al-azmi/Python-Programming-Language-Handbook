import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Functions Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 02: Write a function that takes a list of numbers and returns the minimum, maximum and sum together, then unpack the returned tuple.
    """)
    return


@app.cell
def _():
    def list_stats(numbers):
        return min(numbers), max(numbers), sum(numbers)

    minimum, maximum, total = list_stats([4, 9, 1, 7, 3])
    print(f"Min: {minimum} | Max: {maximum} | Sum: {total}")

    return


if __name__ == "__main__":
    app.run()
