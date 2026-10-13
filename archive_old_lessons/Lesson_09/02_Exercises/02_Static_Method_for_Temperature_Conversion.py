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
        Exercise 02: Create a class with a static method that converts a temperature from Celsius to Fahrenheit without using any object or class data.
    """)
    return


@app.cell
def _():
    class Temperature:
        @staticmethod
        def celsius_to_fahrenheit(celsius):
            return celsius * 9 / 5 + 32

    print(Temperature.celsius_to_fahrenheit(0))
    print(Temperature.celsius_to_fahrenheit(100))
    return


if __name__ == "__main__":
    app.run()
