import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Basics")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Operators and Math Functions
    In this notebook you will learn the arithmetic, relational, logical, bitwise and assignment operators, and use the math module and the ord and chr functions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Arithmetic operators
    `+` addition, `-` subtraction, `*` multiplication, `/` division (always a float), `//` floor division, `%` remainder and `**` power.
    """)
    return


@app.cell
def _():
    _a = 17
    _b = 5
    print(_a + _b, _a - _b, _a * _b)
    print(_a / _b, _a // _b, _a % _b, _a**_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Assignment operators
    `+=`, `-=`, `*=`, `/=`, `//=`, `%=` and `**=` update a variable using its current value.
    """)
    return


@app.cell
def _():
    n = 10
    n += 5
    print(n)
    n *= 2
    print(n)
    n //= 4
    print(n)
    n **= 2
    print(n)

    return (n,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Relational operators
    Relational operators compare two values and give a bool: `==`, `!=`, `<`, `>`, `<=` and `>=`.
    """)
    return


@app.cell
def _():
    _a = 17
    _b = 5
    print(_a == _b, _a != _b, _a < _b, _a > _b, _a <= 17, _b >= 6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Logical operators
    `and`, `or` and `not` combine boolean values. `and` is True only if both sides are True, `or` is True if at least one side is True.
    """)
    return


@app.cell
def _():
    _age = 21
    print(_age > 18 and _age < 30)
    print(_age < 18 or _age == 21)
    print(not _age > 18)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Bitwise operators
    Bitwise operators work on the binary digits of integers: `&` and, `|` or, `^` xor, `~` not, `<<` shift left and `>>` shift right.
    """)
    return


@app.cell
def _():
    _a = 12  # 1100
    _b = 10  # 1010
    print(_a & _b, _a | _b, _a ^ _b, ~_a)
    print(_a << 2, _a >> 2)
    print(format(_a & _b, "04b"), format(_a | _b, "04b"))
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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
