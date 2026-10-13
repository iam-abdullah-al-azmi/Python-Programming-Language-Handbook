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
        Exercise 07: Merge two dictionaries into a new one; if a key exists in both, the value from the second dictionary wins.
    """)
    return


@app.cell
def _():
    first = {"a": 1, "b": 2, "c": 3}
    second = {"c": 30, "d": 40}
    merged = {}
    for key, value in first.items():
        merged[key] = value
    for key, value in second.items():
        merged[key] = value
    print(merged)
    return


if __name__ == "__main__":
    app.run()
