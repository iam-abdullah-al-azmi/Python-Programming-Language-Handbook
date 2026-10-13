import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="User Input and Formatting")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    Taking user input
    """)
    return


@app.cell
def _():
    # length = int(input("Enter the length: "))
    # breadth = int(input("Enter the breadth: "))

    # area = length * breadth
    # print("The area of the rectangle is:", area)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    - When using input function, the input is taken as a string by default. To convert it to an integer, we use the int() function. If we want to take float input, we can use the float() function and others accordingly.

    - To get an expected input, we can use eval() function. For example, if we want to take a list as input, we can use eval(input()).
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
def _():
    _d = 34.44456968
    _d = format(_d, ".3f")  # This will round the number to 3 decimal places
    print(_d, type(_d))
    return


@app.cell
def _():
    _d = 34.44456968
    _d = format(
        _d, "7.3f"
    )  # This will round the number to 3 decimal places and make the total length 7 by adding spaces in the front if necessary
    print(_d, len(_d), type(_d))
    print(" " in _d)
    print(f"{_d.find(' ')}")
    return


@app.cell
def _():
    x = 20.345123
    x = format(
        x, "<7.3f"
    )  # This will round the number to 3 decimal places and make the total length 7 by adding spaces in the back if necessary
    print(x, len(x))
    return


@app.cell
def _():
    from math import pi

    print(pi, format(pi, ".3%"), type(pi))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Specifier Format

    - '10.2f' ---> floating point number with precision 2 and width 10.
    - '<10.2f' ---> Left Justify the floating point number.
    - '>10.2f' ---> Right Justify the formatted item.
    - '10X' ---> Format integer in hexadecimal with width 10
    - '20s' ---> Format String with width 20
    - '10.2%' ---> Format the number in decimal
    """)
    return


@app.cell
def _():
    _val = 344
    print(format(_val, "10X"))
    return


@app.cell
def _():
    characters = "characters"
    print(format(characters, ".5s"), format(characters, "5s"))
    print(len(characters))
    return


if __name__ == "__main__":
    app.run()
