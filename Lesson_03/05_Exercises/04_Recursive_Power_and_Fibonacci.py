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
    Exercise 04: Write a recursive function power(base, exponent) that computes base raised to a non-negative whole exponent without using the ** operator, and a recursive function that returns the n-th Fibonacci number.
    """)
    return


@app.cell
def _():
    def power(base, exponent):
        if exponent == 0:
            return 1
        return base * power(base, exponent - 1)

    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    print(power(2, 10))
    print(power(5, 3))
    print(fibonacci(10))

    return


if __name__ == "__main__":
    app.run()
