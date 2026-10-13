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
        Exercise 03: Find the largest and the smallest number in a list using a for loop.
    """)
    return


@app.cell
def _():
    numbers = [14, 3, 27, 9, 41, 18]
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    print(f"List: {numbers}")
    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
    return


if __name__ == "__main__":
    app.run()
