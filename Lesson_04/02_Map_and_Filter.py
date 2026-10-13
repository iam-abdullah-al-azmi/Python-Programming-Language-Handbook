import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Functional Tools and Generators")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Map and Filter
    `map()` applies a function to every item of a collection, and `filter()` keeps only the items that pass a test. You will use both with lambda functions to transform and select data.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## `map()`
    `map(function, iterable)` runs one function on every single value and returns a lazy `map` object. Wrap it in `list()` to see the results. We build the list of odd numbers with `list(range(...))`, where `range(1, 40, 2)` counts from 1 up to 39 in steps of 2.
    """)
    return


@app.cell
def _():
    lst = list(range(1, 40, 2))
    print(lst)

    sqr = lambda x: x**2
    sqr_list = list(map(sqr, lst))
    print(sqr_list)

    return (lst,)


@app.cell
def _(mo):
    mo.md(r"""
    The function can also be written directly inside `map()`. Here it uses a conditional expression: even numbers are squared, odd multiples of 3 are cubed, and the rest stay as they are.
    """)
    return


@app.cell
def _(lst):
    sqr_list_cond = list(map(lambda val: val**2 if val % 2 == 0 else (val**3 if val % 3 == 0 else val), lst))
    print(sqr_list_cond)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## `map()` on a string
    A string is a sequence of characters, so `map()` can process it character by character. Passing the existing method `str.upper` as the function converts each character to upper case. `"".join(...)` then glues the characters back into one string.
    """)
    return


@app.cell
def _():
    text = "Hello world, Welcome to the age of artificial intelligence (AI)"

    upper_chars = list(map(str.upper, text))
    print(upper_chars)

    upper_text = "".join(upper_chars)
    print(upper_text)

    return text, upper_text


@app.cell
def _(mo):
    mo.md(r"""
    ## `filter()`
    `filter(function, iterable)` is a powerful way to separate data. The function must return `True` or `False` for each item, and only the items that give `True` are kept. First look at what happens if we use `map()` with a test: we get the True/False answers, not the filtered values.
    """)
    return


@app.cell
def _():
    numbers = list(range(2, 50, 2))
    print(numbers[-1])

    answers = list(map(lambda val: val % 2 == 0, numbers))
    print(answers)

    return (numbers,)


@app.cell
def _(mo):
    mo.md(r"""
    With `filter()` the numbers that pass the test are kept.
    """)
    return


@app.cell
def _(numbers):
    even = list(filter(lambda val: val % 2 == 0, numbers))
    print(even)

    greater_than_20 = list(filter(lambda val: val > 20, numbers))
    print(greater_than_20)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## `filter(None, ...)`
    If you pass `None` instead of a function, `filter()` removes every value that Python considers false: `0`, `""`, `None`, `False` and empty collections. This is a quick way to clean data.
    """)
    return


@app.cell
def _():
    data = [1, "", None, None, True, False]

    cleaned_data = list(filter(None, data))
    print(cleaned_data)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## `filter()` on a string
    Using the upper case string from before, keep only the vowels.
    """)
    return


@app.cell
def _(upper_text):
    vowels = list(filter(lambda ch: ch in "aAeEiIoOuU", upper_text))
    print(vowels)

    return


@app.cell
def _(mo):
    mo.md(r"""
    To see each vowel only once, we loop through the result and add a letter only when it is not already in the new list.
    """)
    return


@app.cell
def _(vowels):
    unique_vowels = []
    for _vowel in vowels:
        if _vowel not in unique_vowels:
            unique_vowels.append(_vowel)
    print(unique_vowels)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Using both together
    The output of one can feed the next. Here we square every number and then keep only the squares that are bigger than 20.
    """)
    return


@app.cell
def _():
    small = [1, 2, 3, 4, 5, 6]
    squares = list(map(lambda v: v**2, small))
    big_squares = list(filter(lambda v: v > 20, squares))
    print(squares)
    print(big_squares)

    return


if __name__ == "__main__":
    app.run()
