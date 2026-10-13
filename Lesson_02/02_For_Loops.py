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
    # For Loops
    In this notebook you will repeat actions with the for loop and the range function, use break and continue, and solve small problems such as sums, multiplication tables and perfect numbers.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Looping with range
    `range(start, stop, step)` produces the numbers from start up to, but not including, stop. If only one number is given it is the stop and the start is 0.
    """)
    return


@app.cell
def _():
    for _i in range(5):
        print(_i, end=" ")
    print()
    for _i in range(1, 6):
        print(_i, end=" ")
    print()
    for _i in range(0, 20, 5):
        print(_i, end=" ")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Sum of the numbers from 0 to 10
    A variable outside the loop collects the result (an accumulator). Printing with `end="|"` keeps the numbers on one line.
    """)
    return


@app.cell
def _():
    sum_of_num = 0

    for _num in range(0, 11):
        sum_of_num += _num
        print(_num, end="|")

    print()
    print("Sum:", sum_of_num)

    return (sum_of_num,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Numbers in reversed order
    A negative step counts downwards.
    """)
    return


@app.cell
def _():
    print("Number from 1 to 10 reverse order:")
    for _i in range(10, 0, -1):
        print(_i, end=" ")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Looping over a string
    A for loop can also take the characters of a string one by one.
    """)
    return


@app.cell
def _():
    for _ch in "Python":
        print(_ch, end="-")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Even sum of numbers
    An if statement inside the loop lets us pick only some numbers.
    """)
    return


@app.cell
def _():
    _ev_num = 10
    _ev_sum = 0
    for _i in range(1, _ev_num + 1):
        if _i % 2 == 0:
            _ev_sum += _i
    print(f"Even sum up to {_ev_num} is {_ev_sum}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Sum of numbers using different conditions
    Add only the numbers that are not divisible by 2, 3 or 5.
    """)
    return


@app.cell
def _():
    _nums = 30
    _sums = 0
    for _i in range(1, _nums + 1):
        if _i % 2 != 0 and _i % 3 != 0 and (_i % 5 != 0):
            _sums += _i
    print(_sums)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Multiplication table
    """)
    return


@app.cell
def _():
    _multiplication_table = 7
    print(f"Multiplication table of {_multiplication_table}")
    for _i in range(1, 11):
        print(_multiplication_table, "*", _i, "=", _multiplication_table * _i)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Printing characters with ASCII codes
    The ord function gives the ASCII code of a character and chr converts a code back to a character. Here we print the characters from A to G using a for loop.
    """)
    return


@app.cell
def _():
    _ascii_code = ord("A")
    _end_code = _ascii_code + 6
    for _code in range(_ascii_code, _end_code + 1):
        print(f"Character: {chr(_code)} | ASCII code: {_code}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Variable names from A to G
    This task is a bit of fun: it takes a city name for each letter from A to G. The input is commented out so that the notebook can run without the keyboard; here a placeholder is used.
    """)
    return


@app.cell
def _():
    for _site in range(ord("A"), ord("G") + 1):
        # city = input("Enter a city name: ")
        _city = "City" + chr(_site)
        print(f"City name: {_city} | Variable name: {chr(_site)}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Perfect number
    A perfect number equals the sum of its divisors smaller than itself, for example 6 = 1 + 2 + 3.
    """)
    return


@app.cell
def _():
    _perfect_num = 28
    _perfect_sum = 0
    for _i in range(1, _perfect_num):
        if _perfect_num % _i == 0:
            _perfect_sum += _i

    if _perfect_num == _perfect_sum:
        print(f"{_perfect_num} is a perfect number")
    else:
        print(f"{_perfect_num} is not a perfect number")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## break and continue
    - break stops the loop immediately.
    - continue skips the rest of the current round and goes to the next one.
    """)
    return


@app.cell
def _():
    for _i in range(1, 10):
        if _i == 3:
            continue
        if _i == 7:
            break
        print(_i, end=" ")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Counting even, odd, positive and negative numbers
    Keep one counter for each kind of number and update the right ones inside the loop. A number can belong to two groups at once, for example 4 is even and positive, so the two checks are separate if statements.
    """)
    return


@app.cell
def _():
    # _count = int(input())
    # n_list = list(map(int, input().split()))   # for example: 5 numbers typed in one line
    _even = 0
    _odd = 0
    _pos = 0
    _neg = 0

    for _num in range(-3, 8):
        if _num % 2 == 0:
            _even = _even + 1
        else:
            _odd = _odd + 1
        if _num > 0:
            _pos = _pos + 1
        elif _num < 0:
            _neg = _neg + 1

    print(f"Even: {_even}\nOdd: {_odd}\nPositive: {_pos}\nNegative: {_neg}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## continue: skipping even numbers
    Even numbers are skipped with continue, so only the odd numbers are added to the total.
    """)
    return


@app.cell
def _():
    _total = 0

    for _i in range(1, 11):
        print(_i, "is processing")
        if _i % 2 == 0:
            continue
        print(_i, "is added to the sum")
        _total = _total + _i

    print("Total sum is:", _total)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## break: stopping when a goal is reached
    The loop is allowed to run 20 times, but break stops it as soon as the accuracy reaches 100.
    """)
    return


@app.cell
def _():
    _acc = 95
    _rounds = 0

    for _i in range(20):
        _acc = _acc + 1
        _rounds = _rounds + 1
        print("Current accuracy:", _acc)
        if _acc == 100:
            print("Accuracy reached 100%")
            break

    print("Total iterations:", _rounds)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Predict the output: break and continue
    Work out what each loop prints before running it. Remember that break leaves only the innermost loop it is written in.
    """)
    return


@app.cell
def _():
    # break inside a nested loop only ends the inner loop
    for _i in range(2):
        for _k in range(3):
            if _k == 1:
                break
            print(_i, _k)
    return


@app.cell
def _():
    # after the loop, the variable keeps the value from the last round that ran
    for _i in range(3):
        if _i == 1:
            break
    print(_i)
    return


@app.cell
def _():
    # the loop stops at the first odd number, so only the evens before it are counted
    _count = 0
    for _n in range(1, 6):
        if _n % 2 != 0:
            break
        _count = _count + 1
    print(_count)
    return


@app.cell
def _():
    # continue skips even numbers, break stops at 3
    for _i in range(5, 0, -1):
        if _i % 2 == 0:
            continue
        if _i == 3:
            break
        print(_i)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## for with else
    The else block of a loop runs when the loop finished without meeting a break. This is handy for searching.
    """)
    return


@app.cell
def _():
    for _i in range(2, 6):
        if 24 % _i == 5:
            print("found")
            break
    else:
        print("no number from 2 to 5 leaves remainder 5 with 24")
    return


if __name__ == "__main__":
    app.run()
