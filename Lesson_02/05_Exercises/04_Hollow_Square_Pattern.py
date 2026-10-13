import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Conditionals and Loops Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 04: Print a hollow square pattern of size 5 using the + symbol.
    """)
    return


@app.cell
def _():
    n = 5
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            if i == 1 or i == n or k == 1 or k == n:
                print("+", end=" ")
            else:
                print(" ", end=" ")
        print()

    return (n, i, k)


if __name__ == "__main__":
    app.run()
