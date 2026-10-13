import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Basics Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 04: Convert a given number to binary, octal, and hexadecimal using the format function. Then show the square root of the number rounded up with the math module, and the result of a bitwise AND with 15.
    """)
    return


@app.cell
def _():
    import math

    num = 255
    print(
        f"Decimal: {num} | Binary: {format(num, 'b')} | Octal: {format(num, 'o')} | Hexadecimal: {format(num, 'X')}"
    )
    print(f"Square root rounded up: {math.ceil(math.sqrt(num))}")
    print(f"{num} & 15 = {num & 15} (binary {format(num & 15, 'b')})")
    return


if __name__ == "__main__":
    app.run()
