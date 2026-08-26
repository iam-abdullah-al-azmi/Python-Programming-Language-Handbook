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
        Excercise 08: Here, you have to take an input from the user and convert it to an integer.
    """)
    return


@app.cell
def _():
    _val = input("Enter a number: ")
    print(f"Value before conversion: {_val} | Type: {type(_val)}")

    _val = int(_val)
    print(f"Value after conversion: {_val} | Type: {type(_val)}")
    return


if __name__ == "__main__":
    app.run()
