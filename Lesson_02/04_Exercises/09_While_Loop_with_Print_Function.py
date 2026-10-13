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
        Excercise 05: Suppose you have given an character "A", and your task is to print from A to G. You can not use manual process rather you have to use the ASCII code and a while loop to print all of them.
    """)
    return


@app.cell
def _():
    ascii_code = ord("A")
    end_code = ascii_code + 6

    while ascii_code < end_code:
        print(f"Character: {chr(ascii_code)} | ASCII code: {ascii_code}")
        ascii_code += 1
    return


if __name__ == "__main__":
    app.run()
