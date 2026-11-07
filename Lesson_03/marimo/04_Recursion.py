import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Functions")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Recursion
    A recursive function is a function that calls itself to solve a smaller version of the same problem. You will learn the two parts every recursive function needs, a base case and a recursive case, through a few classic examples.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## The idea
    Every recursive function needs:

    - a **base case**: a situation simple enough to answer directly, which stops the recursion
    - a **recursive case**: a call to the same function with a smaller input that moves towards the base case

    Without a base case the function would call itself forever (Python stops this with a `RecursionError`).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Counting down
    The base case is `n == 0`. Each call prints one number and then calls itself with `n - 1`.
    """)
    return


@app.cell
def _():
    def count_down(n):
        if n == 0:
            print("Go!")
        else:
            print(n)
            count_down(n - 1)


    count_down(5)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Factorial
    The factorial of `n` (written `n!`) is `n * (n-1) * ... * 1`, and `0! = 1`. It can be described recursively: `n! = n * (n-1)!`.
    """)
    return


@app.cell
def _():
    def factorial(n):
        if n == 0:  # base case
            return 1
        return n * factorial(n - 1)  # recursive case


    print(factorial(5))
    print(factorial(10))

    return (factorial,)


@app.cell
def _(mo):
    mo.md(r"""
    Tracing `factorial(3)`: it becomes `3 * factorial(2)`, then `3 * 2 * factorial(1)`, then `3 * 2 * 1 * factorial(0)`, and finally `3 * 2 * 1 * 1 = 6`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Sum of digits
    The sum of the digits of a number is its last digit plus the sum of the digits of the rest of the number. We get the last digit with `% 10` and the rest with `// 10`.
    """)
    return


@app.cell
def _():
    def digit_sum(n):
        if n < 10:  # base case: a single digit
            return n
        return n % 10 + digit_sum(n // 10)


    print(digit_sum(12345))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Fibonacci numbers
    Each Fibonacci number is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8, ... This one has two base cases and two recursive calls.
    """)
    return


@app.cell
def _():
    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)


    for i in range(10):
        print(fibonacci(i), end=" ")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Recursion versus a loop
    Anything done with recursion can also be done with a loop. Recursion is often shorter to write, but a loop is usually faster and avoids the recursion limit. Python allows about 1000 nested calls by default.
    """)
    return


@app.cell
def _(factorial):
    def factorial_loop(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


    print(factorial_loop(5))
    print(factorial_loop(5) == factorial(5))

    return


if __name__ == "__main__":
    app.run()
