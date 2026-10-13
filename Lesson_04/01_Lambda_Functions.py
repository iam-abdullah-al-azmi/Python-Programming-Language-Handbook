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
    # Lambda Functions
    A lambda function is a small, anonymous function written in a single line. You will learn its syntax, how it compares with a regular `def` function, and when it is useful.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Syntax
    A lambda is special, anonymous and inline: `lambda parameters: expression`. There can be many parameters but only one expression, and the value of that expression is returned automatically, so there is no `return` keyword.
    """)
    return


@app.cell
def _():
    sqr_sum = lambda x, y: x**2 + y**2
    print(sqr_sum(2, 3))

    return


@app.cell
def _(mo):
    mo.md(r"""
    The lambda above does exactly the same thing as this regular function.
    """)
    return


@app.cell
def _():
    def sqr_sum_def(x, y):
        return x**2 + y**2


    print(sqr_sum_def(2, 3))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Lambdas that return a True or False answer
    A lambda can contain a comparison. This is very common because tools such as `filter()` (next notebook) need small yes/no functions.
    """)
    return


@app.cell
def _():
    chk_even = lambda x: x % 2 == 0
    print(chk_even(10))
    print(chk_even(11))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Conditions and default values
    A lambda can use a one-line conditional expression, and its parameters can have default values just like a normal function.
    """)
    return


@app.cell
def _():
    bigger = lambda a, b: a if a > b else b
    print(bigger(7, 12))

    add_ten = lambda value, extra=10: value + extra
    print(add_ten(5))
    print(add_ten(5, 20))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Calling a lambda immediately
    Because a lambda is an expression, you can also write it in brackets and call it on the spot without giving it a name.
    """)
    return


@app.cell
def _():
    print((lambda x, y: x * y)(6, 7))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Passing a lambda to another function
    The real strength of a lambda is passing it as an argument to a function that expects another function. The built-in `sorted()` accepts a `key` function that decides what to compare. Here the words are sorted by their length.
    """)
    return


@app.cell
def _():
    words = ["banana", "fig", "cherry", "kiwi"]
    print(sorted(words, key=lambda word: len(word)))

    return


if __name__ == "__main__":
    app.run()
