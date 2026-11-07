import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Conditionals and Loops Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 02: Find the sum of all even numbers from 1 to a given number using a for loop and an if statement.
    """)
    return


@app.cell(hide_code=True)
def _():
    ev_num = 10  # ev_num = int(input("Enter a number:"))
    ev_sum = 0
    for _i in range(1, ev_num + 1):
        if _i % 2 == 0:
            ev_sum += _i
    print(f"Even sum is {ev_sum}")

    return (ev_num, ev_sum)


if __name__ == "__main__":
    app.run()
