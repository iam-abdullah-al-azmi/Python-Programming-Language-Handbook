import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Basics")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Variables and Data Types
    In this notebook you will learn how to store values in variables, how to name them, and what the basic data types int, float, str, bool and complex are. You will also learn to convert between types.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Variable declaration
    A variable is a name that refers to a value. We create it with the assignment operator `=`; no type needs to be declared.
    """)
    return


@app.cell
def _():
    a = 30
    b = 20

    a, b

    return (a, b)


@app.cell
def _(mo):
    mo.md(r"""
    Several variables can be assigned at once, and values can be swapped without a temporary variable.
    """)
    return


@app.cell
def _():
    _x, _y, _z = 1, 2, 3
    _p = _q = 0
    print(_x, _y, _z, _p, _q)

    _x, _y = _y, _x
    print(_x, _y)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Naming rules
    - A name can contain letters, digits and underscores, but cannot start with a digit.
    - Names are case sensitive: `age` and `Age` are different variables.
    - Keywords are reserved words and cannot be used as names. An identifier is a name used to identify a variable, function, class or other objects.
    - Keywords: and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield
    """)
    return


@app.cell
def _():
    import keyword

    print(len(keyword.kwlist), keyword.kwlist)

    return (keyword,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Data types
    Python offers an inbuilt function called type to know the exact type of any value. Everything in Python is an object.

    - int ---> whole numbers
    - float ---> numbers with a decimal point
    - str ---> text
    - bool ---> True or False
    - complex ---> numbers with a real and an imaginary part
    """)
    return


@app.cell
def _():
    print(type(18), type(21.98), type("Hello"), type(True), type(3 + 4j))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Literals
    A literal is a value written directly in the code: integer literal `18`, floating point literal `21.98`, character literal `"Q"` and string literal `"Hello"`. Python tokens are keywords, identifiers (variables), operators, delimiters and literals.
    """)
    return


@app.cell
def _():
    age = 21
    height = 1.75
    name = "Azmi"
    is_student = True
    number = 2 + 3j

    print(name, age, height, is_student, number)
    print(number.real, number.imag)

    return (age, height, name, is_student, number)


@app.cell
def _(mo):
    mo.md(r"""
    ## Type conversion
    - The int function converts a string or a number into a whole number (a float is cut, not rounded).
    - The float function converts a string or an integer into a floating-point number.
    - The str function converts any value into text.
    - The bool function converts a value into a boolean; 0, 0.0 and the empty string become False and everything else becomes True.
    """)
    return


@app.cell
def _():
    print(int("42"), int(9.99), float("3.5"), float(7), str(100), str(2.5))
    print(bool(0), bool(5), bool(""), bool("False"))
    print(type(int("42")), type(str(100)))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Checking a type
    Besides type, the isinstance function answers whether a value belongs to a given type.
    """)
    return


@app.cell
def _():
    print(isinstance(10, int), isinstance(10, float), isinstance("10", str))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Summary

    1. type() gives the exact type of any value.
    2. Keywords are reserved words and cannot be used as identifiers or variable names.
    3. Everything in Python is an object.
    4. int() converts a string or a number into an integer; float() converts into a floating-point number.
    5. The Boolean data type is represented in Python as bool.
    6. print() displays contents on the screen, input() accepts input from the user and format() returns a formatted string.
    """)
    return


if __name__ == "__main__":
    app.run()
