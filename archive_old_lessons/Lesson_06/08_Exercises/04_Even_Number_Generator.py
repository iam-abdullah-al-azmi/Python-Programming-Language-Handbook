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
        Exercise 04: Write a generator function that yields the even numbers up to a given limit, and use next() and a for loop to read values from it.
    """)
    return


@app.cell
def _():
    def even_numbers(limit):
        for number in range(2, limit + 1, 2):
            yield number

    evens = even_numbers(10)
    print(next(evens))
    print(next(evens))
    for number in evens:
        print(number, end=" ")
    print()
    return


if __name__ == "__main__":
    app.run()
