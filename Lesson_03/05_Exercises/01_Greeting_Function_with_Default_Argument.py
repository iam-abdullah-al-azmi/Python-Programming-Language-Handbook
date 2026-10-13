import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Functions Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 01: Write a function that greets a person by name. If no name is given, it should greet 'Guest' by default.
    """)
    return


@app.cell
def _():
    def greet(name="Guest"):
        return f"Hello, {name}!"

    print(greet("Azmi"))
    print(greet())

    return


if __name__ == "__main__":
    app.run()
