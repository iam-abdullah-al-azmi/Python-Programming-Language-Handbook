import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Conditionals and Loops")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Nested Loops and Pattern Printing
    In this notebook you will put one loop inside another and use it to print number, letter and symbol patterns. The outer loop controls the rows and the inner loop controls the columns.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## How nested loops run
    For every single round of the outer loop, the inner loop runs completely. Calling print() with nothing inside moves the output to the next line. In each pattern below the size is fixed; the original notebook read it with `int(input("Enter the no"))`.
    """)
    return


@app.cell
def _():
    for _i in range(1, 4):
        for _k in range(1, 4):
            print(f"{_i}x{_k}", end="  ")
        print()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Number triangle
    Row i prints the numbers from 1 to i.
    """)
    return


@app.cell
def _():
    _user_want = 5  # int(input("Enter the no"))

    for _i in range(1, _user_want + 1):
        for _k in range(1, _i + 1):
            print(f"{_k}", end="")

        print()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Continuing number triangle
    A counter outside the loops keeps increasing, so the numbers continue from row to row.
    """)
    return


@app.cell
def _():
    _user_want = 5
    _count = 1

    for _i in range(1, _user_want + 1):
        for _k in range(1, _i + 1):
            print(f"{_count}", end="")
            _count += 1

        print()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inverted number triangle
    Counting the outer loop downwards makes the rows shorter.
    """)
    return


@app.cell
def _():
    _user_want = 5

    for _i in range(_user_want, 0, -1):
        for _k in range(1, _i + 1):
            print(f"{_k}", end="")

        print()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Letter triangle
    The chr function turns an ASCII code into a letter, so the pattern continues A, B, C, ...
    """)
    return


@app.cell
def _():
    _user_want = 5
    _letter = 65

    for _i in range(1, _user_want + 1):
        for _k in range(1, _i + 1):
            print(f"{chr(_letter)}", end="")
            _letter += 1

        print()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hollow square pattern
    Print the symbol only in the first and last row and the first and last column; print a space elsewhere.
    """)
    return


@app.cell
def _():
    _user_input = 6

    for _i in range(1, _user_input + 1):
        for _k in range(1, _user_input + 1):
            if _i == 1 or _i == _user_input or _k == 1 or (_k == _user_input):
                print("+", end=" ")
            else:
                print(" ", end=" ")

        print()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inverted and rotated half-pyramid
    Each row first prints some spaces and then the symbols; the spaces decrease while the symbols increase.
    """)
    return


@app.cell
def _():
    _user_input = 5

    for _i in range(1, _user_input + 1):
        _n = _user_input - _i
        for _k in range(1, _n + 1):
            print(" ", end=" ")
        for _k in range(1, _i + 1):
            print("+", end=" ")

        print()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pyramid
    Row i has `n - i` spaces and `2 * i - 1` symbols.
    """)
    return


@app.cell
def _():
    _user_input = 5

    for _i in range(1, _user_input + 1):
        _num_spaces = _user_input - _i
        for _k in range(
            1, _num_spaces + 1
        ):  # no of spaces decrease as the row no increases
            print(" ", end=" ")
        _num_symbols = 2 * _i - 1
        for _k in range(1, _num_symbols + 1):
            print("+", end=" ")

        print()
    return


if __name__ == "__main__":
    app.run()
