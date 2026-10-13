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
        Exercise 06: Count how many numbers in a list are even, odd, positive and negative.
    """)
    return


@app.cell
def _():
    n_list = [5, -2, 0, 8, -7, 3, 10, -4]
    even = 0
    odd = 0
    pos = 0
    neg = 0
    for num in n_list:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
    print(f"Even: {even}\nOdd: {odd}\nPositive: {pos}\nNegative: {neg}")
    return


if __name__ == "__main__":
    app.run()
