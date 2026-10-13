import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Exceptions, Files and Modules Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 01: Write a function that divides two values and handles ZeroDivisionError and TypeError separately. Test it with valid and invalid inputs.
    """)
    return


@app.cell
def _():
    def safe_divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"
        except TypeError:
            return "Both values must be numbers"
        else:
            return result

    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide(10, "two"))
    return


if __name__ == "__main__":
    app.run()
