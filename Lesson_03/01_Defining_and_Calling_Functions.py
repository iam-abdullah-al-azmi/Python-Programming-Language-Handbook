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
    # Defining and Calling Functions
    A function is a named block of code that you write once and run whenever you need it. In this notebook you will learn how to define a function with `def`, call it, and give it parameters, including default values.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Defining a function and calling it
    A function is defined with the `def` keyword, a name, parentheses holding its parameters, and a colon. The indented lines below it are the body. Nothing runs until the function is called by writing its name followed by parentheses.
    """)
    return


@app.cell
def _():
    def greet_language(lang):
        print(f"Welcome to the World of {lang}")


    greet_language("Python")

    return (greet_language,)


@app.cell
def _(mo):
    mo.md(r"""
    The value you pass when calling (`"Python"`) is called an **argument**, and the name in the definition (`lang`) is called a **parameter**. You can call the same function as many times as you like with different arguments.
    """)
    return


@app.cell
def _(greet_language):
    greet_language("C++")
    greet_language("Perl")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Default arguments
    A parameter can be given a default value. If the caller does not pass anything for it, the default is used. If the caller does pass a value, it replaces the default.
    """)
    return


@app.cell
def _():
    def greet_default(lang="C++"):
        print(f"Welcome to the World of {lang}")


    greet_default()
    greet_default("Perl")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Several parameters and positional arguments
    A function can take any number of parameters. When you call it, the arguments are matched to the parameters by **position**, so the order matters.
    """)
    return


@app.cell
def _():
    def show_values(a, b, c):
        print(f"a={a} | b={b} | c={c}")


    show_values(10, 20, 30)
    show_values(30, 20, 10)

    return (show_values,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Keyword arguments
    If you write the parameter name along with the value, you do not have to care about the position any more. This is called a **keyword argument**.
    """)
    return


@app.cell
def _(show_values):
    show_values(b=10, c=20, a=30)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## A function that prints instead of returning
    The function below only prints the result. It does not hand anything back to the caller, so Python gives back the special value `None`. Trying to use that result in a calculation causes an error. The next notebook shows how `return` solves this.
    """)
    return


@app.cell
def _():
    def sqr_summation(a, b, c):
        summation = a**2 + b**2 + c**2
        print(f"Summation of {a}, {b} and {c} is {summation}")


    result = sqr_summation(10, 20, 30)
    print(result)

    # result + 10 would raise a TypeError because None cannot be added to an integer

    return


if __name__ == "__main__":
    app.run()
