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
    Exercise 03: Reverse the digits of a given number using a while loop.
    """)
    return


@app.cell
def _():
    temp_num = 12345  # temp_num = eval(input("Enter a number: "))
    sum_of_reversed = 0
    while temp_num > 0:
        rem = temp_num % 10
        sum_of_reversed = sum_of_reversed * 10 + rem
        temp_num = temp_num // 10
    print(sum_of_reversed)

    return (temp_num, sum_of_reversed, rem)


if __name__ == "__main__":
    app.run()
