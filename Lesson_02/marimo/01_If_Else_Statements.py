import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Conditionals and Loops")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # If-Else Statements
    In this notebook you will make your programs take decisions with if, elif and else, combine conditions with logical operators, and use nested conditions.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## The if statement
    An if statement runs its indented block only when the condition is True. The block is defined by indentation.
    """)
    return


@app.cell
def _():
    temperature = 32
    if temperature > 30:
        print("It is a hot day")
    print("This line always runs")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## if and else
    else runs when the condition is False.
    """)
    return


@app.cell
def _():
    number = 7
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## elif
    When there are more than two possibilities, use elif (else if). Python checks the conditions from top to bottom and runs only the first block whose condition is True.
    """)
    return


@app.cell
def _():
    score = 76
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    print(f"Score: {score} | Grade: {grade}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Conditions with logical operators
    Use and, or and not to build a condition from smaller ones.
    """)
    return


@app.cell
def _():
    year = 2024
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Nested if
    An if statement can be placed inside another one. The inner condition is checked only if the outer condition is True.
    """)
    return


@app.cell
def _():
    age = 25
    has_id = True
    if age >= 18:
        if has_id:
            print("Entry allowed")
        else:
            print("Please show an ID")
    else:
        print("Too young")
    return


@app.cell
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
    num_1 = 7
    num_2 = 3
    num_3 = 9

    max_num = num_1

    if num_2 > max_num:
        max_num = num_2
    if num_3 > max_num:
        max_num = num_3

    min_num = num_1

    if num_2 < min_num:
        min_num = num_2
    if num_3 < min_num:
        min_num = num_3

    print(min_num, max_num)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Predict the output
    Read the code and decide what it prints before you run it. Only the first condition that is true runs, and the rest are skipped.
    """)
    return


@app.cell
def _():
    x = 5
    if x > 3:
        print("A")
    elif x > 1:
        print("B")
    else:
        print("C")
    return


@app.cell
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


@app.cell
def _(mo):
    mo.md(r"""
    ## Conditional expression
    A short if-else can be written on one line: `value_if_true if condition else value_if_false`.
    """)
    return


@app.cell
def _():
    y = 10
    label = "even" if y % 2 == 0 else "odd"
    print(y, "is", label)
    return


if __name__ == "__main__":
    app.run()
