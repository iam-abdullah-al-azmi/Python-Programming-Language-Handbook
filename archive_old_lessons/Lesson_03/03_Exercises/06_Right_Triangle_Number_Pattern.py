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
        Exercise 06: Print a right triangle number pattern for n = 5 (1, 12, 123, ...).
    """)
    return


@app.cell
def _():
    n = 5
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            print(k, end="")
        print()
    return


if __name__ == "__main__":
    app.run()
