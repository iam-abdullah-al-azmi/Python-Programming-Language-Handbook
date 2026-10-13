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
    # Arguments and Scope
    Functions can accept a flexible number of arguments using `*args` and `**kwargs`, and variables behave differently inside and outside a function. You will learn the rules of local and global scope and how the `global` keyword works.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Mixing positional and default arguments
    Parameters with default values must come after the ones without. This keeps calls readable, since the required values are given first.
    """)
    return


@app.cell
def _():
    def power(base, exponent=2):
        return base**exponent


    print(power(5))
    print(power(5, 3))
    print(power(exponent=4, base=2))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Any number of arguments with `*args`
    If you do not know how many values will be passed, put a `*` in front of a parameter name (conventionally `args`). Python collects all the extra positional arguments into a tuple, which you can loop over.
    """)
    return


@app.cell
def _():
    def sqr_sum(*args):
        """Return the sum of the squares of all the given numbers."""
        print(f"Value of args [multiple argument]: {args} and type of it {type(args)}")

        total = 0
        for i in range(len(args)):
            total += args[i] ** 2
        return total


    print(sqr_sum(10, 20, 30, 40, 50, 60))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Any number of keyword arguments with `**kwargs`
    Putting `**` in front of a parameter name (conventionally `kwargs`) collects all the extra keyword arguments into a **dictionary**, a collection of `key: value` pairs (covered in Lesson 06). You can read a value with its key, such as `kwargs["marks"]`.
    """)
    return


@app.cell
def _():
    def student_info(**kwargs):
        """Return the total of the marks given as a keyword argument."""
        print(f"Value of keyword args [multiple keyword argument]: {kwargs} and type of it {type(kwargs)}")
        print(kwargs.keys())

        total_marks = 0
        for val in kwargs["marks"]:
            total_marks += val
        return total_marks


    print(student_info(name="marimo", year=10, marks=[280, 270, 295]))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Local scope
    A variable created inside a function is **local**: it exists only while the function runs and cannot be seen from outside.
    """)
    return


@app.cell
def _():
    def make_local():
        secret = 42
        print(f"Inside the function: {secret}")


    make_local()
    # print(secret) would raise a NameError because secret only exists inside make_local

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Global scope
    A variable created outside any function is **global**. A function can read it, but if the function assigns to the same name, Python creates a new local variable and leaves the global one untouched.
    """)
    return


@app.cell
def _():
    counter = 10


    def read_global():
        print(f"Reading the global value: {counter}")


    def shadow_global():
        counter = 99  # a new local variable, not the global one
        print(f"Local value: {counter}")


    read_global()
    shadow_global()
    print(f"Global value after the call: {counter}")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## The `global` keyword
    To change a global variable from inside a function, declare it with `global` first.
    """)
    return


@app.cell
def _():
    total_calls = 0


    def count_call():
        global total_calls
        total_calls += 1


    count_call()
    count_call()
    count_call()
    print(f"The function was called {total_calls} times")

    return


@app.cell
def _(mo):
    mo.md(r"""
    Using `global` is easy to overdo. In most cases it is cleaner to pass values in as arguments and get the result back with `return`.
    """)
    return


@app.cell
def _():
    def add_one(value):
        return value + 1


    number = 5
    number = add_one(number)
    print(number)

    return


if __name__ == "__main__":
    app.run()
