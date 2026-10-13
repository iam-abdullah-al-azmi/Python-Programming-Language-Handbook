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
    # Operators and Math Functions
    In this notebook you will learn the arithmetic, relational, logical, bitwise and assignment operators, and use the math module and the ord and chr functions.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Arithmetic operators
    `+` addition, `-` subtraction, `*` multiplication, `/` division (always a float), `//` floor division, `%` remainder and `**` power.
    """)
    return


@app.cell
def _():
    a = 17
    b = 5
    print(a + b, a - b, a * b)
    print(a / b, a // b, a % b, a**b)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Assignment operators
    `+=`, `-=`, `*=`, `/=`, `//=`, `%=` and `**=` update a variable using its current value.
    """)
    return


@app.cell
def _():
    c = 10
    c += 5
    print(c)
    c *= 2
    print(c)
    c //= 4
    print(c)
    c **= 2
    print(c)

    return (c,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Relational operators
    Relational operators compare two values and give a bool: `==`, `!=`, `<`, `>`, `<=` and `>=`.
    """)
    return


@app.cell
def _():
    x = 17
    y = 5
    print(x == y, x != y, x < y, x > y, x <= 17, y >= 6)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Logical operators
    `and`, `or` and `not` combine boolean values. `and` is True only if both sides are True, `or` is True if at least one side is True.
    """)
    return


@app.cell
def _():
    age = 21
    print(age > 18 and age < 30)
    print(age < 18 or age == 21)
    print(not age > 18)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Bitwise operators
    Bitwise operators work on the binary digits of integers: `&` and, `|` or, `^` xor, `~` not, `<<` shift left and `>>` shift right.
    """)
    return


@app.cell
def _():
    p = 12  # 1100
    q = 10  # 1010
    print(p & q, p | q, p ^ q, ~p)
    print(p << 2, p >> 2)
    print(format(p & q, "04b"), format(p | q, "04b"))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Operator summary
    Arithmetic: `+ - * / // % **`. Relational: `== != <= >= < >`. Logical: `and not or`. Bitwise: `& | ~ ^ << >>`.

    Python also has built-in numeric functions that need no import: abs, round, pow, min, max, divmod.
    """)
    return


@app.cell
def _():
    print(abs(-7), round(3.14159, 2), round(2.5), pow(2, 10))
    print(min(4, 9, 1), max(4, 9, 1), divmod(17, 5))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## The math module
    To use mathematical functions we import the math module.

    - ceil(x) ----> Round x up to the nearest integer and return that integer.
    - floor(x) ----> Returns the largest integer not greater than x
    - exp(x) ----> Returns the exponential value e^x
    - log(x) ----> Returns the natural logarithm of x (to base e)
    - log(x, base) ----> Returns the logarithm of x to the given base
    - sqrt(x) ----> Return the square root of x
    - sin(x) ----> Return the sine of x, where x is the value in radians
    - asin(x) ----> Return the angle in radians whose sine is x
    - cos(x) ----> Return the cosine of x, where x is the value in radians
    - acos(x) ----> Return the angle in radians whose cosine is x
    - tan(x) ----> Return the tangent of x, where x is the value in radians
    - degrees(x) ----> Convert angle x from radians to degrees
    - radians(x) ----> Convert angle x from degrees to radians
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

    return (math,)


@app.cell
def _(math):
    print(math.sqrt(144), math.log(8, 2), math.pi)
    print(math.sin(math.radians(30)), math.cos(0), math.tan(math.radians(45)))
    print(math.degrees(math.pi), math.degrees(math.asin(1)), math.degrees(math.acos(0)))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ord and chr functions

    - "ord" returns the ASCII (Unicode) value of a character
    - "chr" returns the character of an ASCII value
    """)
    return


@app.cell
def _():
    print(ord("A"), chr(65))
    print(ord("a") - ord("A"), chr(ord("A") + 2))
    return


if __name__ == "__main__":
    app.run()
