import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Functions")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 03: Write a function using *args that returns the sum of any number of values passed to it. Then use a global counter to count how many times the function has been called.
    """)
    return


@app.cell
def _():
    call_count = 0

    def add_all(*args):
        global call_count
        call_count += 1
        total = 0
        for value in args:
            total += value
        return total

    print(add_all(1, 2, 3))
    print(add_all(10, 20, 30, 40, 50))
    print(f"add_all was called {call_count} times")

    return


if __name__ == "__main__":
    app.run()
