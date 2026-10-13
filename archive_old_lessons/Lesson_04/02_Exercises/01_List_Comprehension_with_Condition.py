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
        Exercise 01: Given x = 1, y = 1, z = 2 and n = 3, print all [a, b, c] combinations where a + b + c is not equal to n.
    """)
    return


@app.cell
def _():
    x, y, z, n = 1, 1, 2, 3
    result = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n]
    print(result)
    return


if __name__ == "__main__":
    app.run()
