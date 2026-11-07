import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Exceptions, Files and Modules")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Exception Handling
    Learn how to stop a Python program from crashing when something goes wrong, using `try`, `except`, `else` and `finally`.

    Blog Link: https://www.geeksforgeeks.org/python/python-exception-handling/
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## What happens without handling
    Dividing a number by zero raises a `ZeroDivisionError`. If nothing catches it, the program stops with a traceback.
    Here the error is caught only so that we can look at its message.
    """)
    return


@app.cell
def _():
    _n = 10
    try:
        _res = _n / 0
    except ZeroDivisionError as _error:
        print(f"Without handling the program would stop here. Error message: {_error}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Handling the exception with try and except
    Code that might fail goes inside `try`. If the error named in `except` happens, Python jumps to that block and the program keeps running.
    """)
    return


@app.cell
def _():
    _n = 10
    try:
        _res = _n / 0
    except ZeroDivisionError:
        print(f"{_n} can't divided by zero")
    print("The program continues")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Error versus Exception
    - An error is a serious problem in the program (for example a syntax error) and we cannot handle it while the program runs.
    - An exception is a less severe problem that occurs at runtime and can be managed with exception handling.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## try, except, else and finally
    - `except` runs when the matching exception is raised (we can have several `except` blocks)
    - `else` runs only when no exception was raised
    - `finally` always runs, whether there was an exception or not

    The function below was originally written with `input()`. Here it receives the text as an argument so that we can test several inputs at once.
    """)
    return


@app.cell
def _():
    def divide_100_by(text):
        # text = input()  # in a real program the text comes from the user
        try:
            _n = int(text)
            _res = 100 / _n
        except ZeroDivisionError:
            print(f"100 can't be divided by {text}")
        except ValueError:
            print("Invalid input. Please provide an integer value")
        else:
            print(f"Result is {_res}")
        finally:
            print("Execution is complete")

    for _text in ["4", "0", "abcd"]:
        print(f"--- input: {_text}")
        divide_100_by(_text)

    return (divide_100_by,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Catching several exceptions at once and a bigger example
    Put the exception types in a tuple to handle them with one `except` block. The example below sums the numbers hidden inside a list of mixed values.
    Note that `try-except` cannot be used inside a list comprehension, so a regular loop is needed.
    """)
    return


@app.cell
def _():
    _values = ["23", "abcd", 23, 23.8, "a ", "a b"]

    try:
        # converting string numbers to actual numbers then sum
        # This filters out non-numeric strings like "abcd"
        _numeric_values = []

        for _item in _values:
            if isinstance(_item, (int, float)):
                _numeric_values.append(_item)
            elif isinstance(_item, str):
                if len(_item) == 1:
                    _numeric_values.append(float(ord(_item)))
                elif " " in _item:
                    _item = _item.strip()
                    if len(_item) == 1:
                        _numeric_values.append(float(ord(_item)))
                    else:
                        print(f"{_item} length is greater than one.")
                else:
                    try:
                        _numeric_values.append(float(_item))
                    except Exception as _e:
                        print(f"Error: {_e}")
                        continue

        _summation = sum(_numeric_values)
    except (ValueError, TypeError) as _e:
        print(f"Error: {_e}")
    else:
        print(f"Numeric Values: {_numeric_values} and Sum of the values: {_summation}")
    finally:
        print("Done")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Raising an exception ourselves
    The `raise` statement lets our own code signal a problem.
    """)
    return


@app.cell
def _():
    def set_age(age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age

    try:
        set_age(-5)
    except ValueError as _error:
        print(f"Caught: {_error}")
    return


if __name__ == "__main__":
    app.run()
