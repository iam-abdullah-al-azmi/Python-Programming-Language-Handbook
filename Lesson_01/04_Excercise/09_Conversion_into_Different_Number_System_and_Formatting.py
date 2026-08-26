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
        Excercise 04: Convert a given number to binary, octal, and hexadecimal using the format function.
    """)
    return


@app.cell
def _():
    num = 255
    print(
        f"Decimal: {num} | Binary: {format(num, 'b')} | Octal: {format(num, 'o')} | Hexadecimal: {format(num, 'X')}"
    )
    return


if __name__ == "__main__":
    app.run()
