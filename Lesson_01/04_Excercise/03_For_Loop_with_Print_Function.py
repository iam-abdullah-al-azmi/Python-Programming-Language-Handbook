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
        Excercise 06: Now, the same task of Excercise 05 has to be done but using a for loop.
    """)
    return


@app.cell
def _():
    ascii_code = ord("A")
    end_code = ascii_code + 6

    for code in range(ascii_code, end_code):
        print(f"Character: {chr(code)} | ASCII code: {code}")
    return


if __name__ == "__main__":
    app.run()
