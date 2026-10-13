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
    # Taking Input and Formatting
    In this notebook you will read values typed by the user with the input function, convert them to numbers, and format numbers and text neatly with the format function.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Taking user input
    The input function shows a message and returns what the user typed. The code below is commented out because it waits for the keyboard; remove the `#` to try it.
    """)
    return


@app.cell
def _():
    # length = int(input("Enter the length: "))
    # breadth = int(input("Enter the breadth: "))

    # area = length * breadth
    # print("The area of the rectangle is:", area)
    return


@app.cell
def _(mo):
    mo.md(r"""
    - When using the input function, the input is taken as a string by default. To convert it to an integer, we use the int() function. If we want to take float input, we can use the float() function and others accordingly.

    - To get an expected input, we can use the eval() function. For example, if we want to take a list as input, we can use eval(input()). Be careful: eval runs whatever is typed, so use it only with input you trust.
    """)
    return


@app.cell
def _():
    # number = eval(input("Enter a number: "))
    # strings = input("Enter a string: ")

    # print(number, type(number))
    # print(strings, type(strings))
    return


@app.cell
def _(mo):
    mo.md(r"""
    The next cell imitates what input returns by using a string directly. Notice that the value is text until we convert it.
    """)
    return


@app.cell
def _():
    typed = "25"  # this is what input() would return
    print(typed, type(typed))
    as_int = int(typed)
    as_float = float(typed)
    print(as_int + 5, as_float + 5)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Formatting with the format function
    The format function returns a string. The second argument is a format specifier that says how the value must look.
    """)
    return


@app.cell
def _():
    x = 34.44456968
    x = format(x, ".3f")  # This will round the number to 3 decimal places
    print(x, type(x))
    return


@app.cell
def _():
    y = 34.44456968
    y = format(
        y, "7.3f"
    )  # This will round the number to 3 decimal places and make the total length 7 by adding spaces in the front if necessary
    print(y, len(y), type(y))
    print(" " in y)
    print(f"{y.find(' ')}")
    return


@app.cell
def _():
    z = 20.345123
    z = format(
        z, "<7.3f"
    )  # This will round the number to 3 decimal places and make the total length 7 by adding spaces in the back if necessary
    print(z, len(z))
    return


@app.cell
def _():
    from math import pi

    print(pi, format(pi, ".3%"), type(pi))

    return (pi,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Specifier format

    - '10.2f' ---> floating point number with precision 2 and width 10.
    - '<10.2f' ---> Left justify the floating point number.
    - '>10.2f' ---> Right justify the formatted item.
    - '10X' ---> Format integer in hexadecimal with width 10
    - '20s' ---> Format string with width 20
    - '10.2%' ---> Format the number as a percentage
    """)
    return


@app.cell
def _():
    val = 344
    print(format(val, "10X"))
    return


@app.cell
def _():
    characters = "characters"
    print(format(characters, ".5s"), format(characters, "5s"))
    print(len(characters))

    return (characters,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Number systems
    The same format function can show an integer in binary (`b`), octal (`o`) and hexadecimal (`x` or `X`).
    """)
    return


@app.cell
def _():
    num = 255
    print(format(num, "b"), format(num, "o"), format(num, "x"), format(num, "X"))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## f-strings
    An f-string puts values directly inside the text using curly braces, and accepts the same format specifiers after a colon.
    """)
    return


@app.cell
def _():
    name = "Azmi"
    price = 1234.5678
    print(f"{name} paid ${price:.2f}")
    print(f"[{name:<10}] [{name:>10}] [{price:>12.1f}]")
    return


if __name__ == "__main__":
    app.run()
