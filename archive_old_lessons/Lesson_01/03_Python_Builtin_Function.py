import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Fundamental")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python in-built function

    - ceil(x) ----> Round X to nearest integer and returns that integer.
    - floor(x) ----> Returns the largest value not greater than X
    - exp(x) ----> Returns the exponential value for e^x
    - log(x) ----> Returns the natural logarithmic of x (to base e)
    - log(x, base) ----> Returns the logarithm of x to the given base
    - sqrt(x) ----> Return the square root of x
    - Sin(x) ----> Return the sin of X, where X is the value in radians
    - asin(x) ----> Return the angle in radians for the inverse of sine
    - cos(x) ----> Return the sin of X, where X is the value in radians
    - aCos(x) ----> Return the angle in radians for the inverse of cosine
    - tan(x) ----> Return the tangent of X, where X is the value in radians
    - degrees(x) ----> Convert angle X from to radians to degrees
    - Radians(x) ----> Convert angle X from to radians to degrees
    """)
    return


@app.cell
def _():
    import math

    print(math.ceil(10.23))
    print(math.floor(10.23))
    print(math.exp(2))
    print(format(math.exp(2), ".3f"))
    print(math.log(2.7))
    print(math.floor(math.log(2.7)))
    print(math.ceil(math.log(2.7)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ord and chr functions

    - "ord" return the ASCII value of a character
    - "chr" return the character of ASCII value
    """)
    return


@app.cell
def _():
    print(ord("A"), chr(65))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Summary

    1. Python offers an inbuilt method called type to know the exact type of any value.

    2. Keywords are reserved words.

    3. Keywords cannot be used as identifiers or variables. An identifier is a name used to identify a variable, function, class or other objects.

    4. Everything in Python is an object.

    5. The int function converts a string or a number into a whole number or integer.

    6. The float function converts a string into a floating-point number.

    7. The Boolean data type is represented in Python as of type bool.

    8. print function is used to display contents on the screen.

    9. input() function is used to accept input from the user.

    10. format() function can be used to return a formatted string.

    11. Python Tokens: keywords, identifiers/Variables, Operators, Delimiters, literals

    12. Integer Literal: 18, Floating Point Literal: 21.98, "Q" : Character literal, "Hello": String Literal

    13. keywords: and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return,
    True, try, while, with, yield

    14. Operators: "+ - * / // % ** ---> Arithmetic Operator" "== != <> <= >= ---> Relational Operator" "and not or ---> Logical Operator" "& | ~ ^ << >> ---> Bitwise Operator"

    """)
    return


if __name__ == "__main__":
    app.run()
