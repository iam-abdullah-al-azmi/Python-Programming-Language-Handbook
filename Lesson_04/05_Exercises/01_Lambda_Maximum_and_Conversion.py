import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Functional Tools and Generators")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 01: Write a lambda function that converts a temperature from Celsius to Fahrenheit (F = C * 9 / 5 + 32) and another lambda that returns the larger of two numbers.
    """)
    return


@app.cell
def _():
    to_fahrenheit = lambda c: c * 9 / 5 + 32
    larger = lambda a, b: a if a > b else b

    print(to_fahrenheit(0))
    print(to_fahrenheit(100))
    print(larger(8, 15))
    print(larger(-3, -9))

    return


if __name__ == "__main__":
    app.run()
