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
        Exercise 02: Reverse the order of the elements in a list without using the reverse() method.
    """)
    return


@app.cell
def _():
    numbers = [4, 2, 9, 1, 5, 6]
    reversed_numbers = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_numbers.append(numbers[i])
    print(f"Original list: {numbers}")
    print(f"Reversed list: {reversed_numbers}")
    return


if __name__ == "__main__":
    app.run()
