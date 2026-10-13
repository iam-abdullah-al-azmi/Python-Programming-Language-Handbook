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
    # If-Else Statements
    In this notebook you will make your programs take decisions with if, elif and else, combine conditions with logical operators, and use nested conditions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The if statement
    An if statement runs its indented block only when the condition is True. The block is defined by indentation.
    """)
    return


@app.cell
def _():
    _temperature = 32
    if _temperature > 30:
        print("It is a hot day")
    print("This line always runs")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## if and else
    else runs when the condition is False.
    """)
    return


@app.cell
def _():
    _number = 7
    if _number % 2 == 0:
        print(f"{_number} is even")
    else:
        print(f"{_number} is odd")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## elif
    When there are more than two possibilities, use elif (else if). Python checks the conditions from top to bottom and runs only the first block whose condition is True.
    """)
    return


@app.cell
def _():
    _score = 76
    if _score >= 80:
        _grade = "A"
    elif _score >= 70:
        _grade = "B"
    elif _score >= 60:
        _grade = "C"
    else:
        _grade = "F"
    print(f"Score: {_score} | Grade: {_grade}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conditions with logical operators
    Use and, or and not to build a condition from smaller ones.
    """)
    return


@app.cell
def _():
    _year = 2024
    if (_year % 4 == 0 and _year % 100 != 0) or _year % 400 == 0:
        print(f"{_year} is a leap year")
    else:
        print(f"{_year} is not a leap year")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nested if
    An if statement can be placed inside another one. The inner condition is checked only if the outer condition is True.
    """)
    return


@app.cell
def _():
    _age = 25
    _has_id = True
    if _age >= 18:
        if _has_id:
            print("Entry allowed")
        else:
            print("Please show an ID")
    else:
        print("Too young")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Minimum and maximum of three numbers
    Compare the first number with the others one by one, keeping the biggest (or smallest) seen so far. This is a classic competitive programming (ICPC) problem.
    """)
    return


@app.cell
def _():
    # user_input = input()   # for example: 7 3 9
    # numbers = user_input.split()
    # _num_1 = int(numbers[0])
    # _num_2 = int(numbers[1])
    # _num_3 = int(numbers[2])
    _num_1 = 7
    _num_2 = 3
    _num_3 = 9

    _max_num = _num_1

    if _num_2 > _max_num:
        _max_num = _num_2
    if _num_3 > _max_num:
        _max_num = _num_3

    _min_num = _num_1

    if _num_2 < _min_num:
        _min_num = _num_2
    if _num_3 < _min_num:
        _min_num = _num_3

    print(_min_num, _max_num)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Predict the output
    Read the code and decide what it prints before you run it. Only the first condition that is true runs, and the rest are skipped.
    """)
    return


@app.cell
def _():
    _x = 5
    if _x > 3:
        print("A")
    elif _x > 1:
        print("B")
    else:
        print("C")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Taking the number from the user
    The same checks work with a number typed by the user. The following code is commented out because it waits for the keyboard.

    The factorial example from the old version of this lesson uses a loop, so it appears in the While Loops notebook.
    """)
    return


@app.cell
def _():
    # value = int(input("Enter a number: "))
    # if value > 0:
    #     print("Positive")
    # elif value < 0:
    #     print("Negative")
    # else:
    #     print("Zero")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conditional expression
    A short if-else can be written on one line: `value_if_true if condition else value_if_false`.
    """)
    return


@app.cell
def _():
    _n = 10
    _label = "even" if _n % 2 == 0 else "odd"
    print(_n, "is", _label)
    return


if __name__ == "__main__":
    app.run()
