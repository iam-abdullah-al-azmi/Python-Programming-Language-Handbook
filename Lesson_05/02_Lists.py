import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Strings and Lists")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Lists
    A list is an ordered, changeable collection of items written inside square brackets. You will learn how to create lists, read items by index, slice them, change them and store different types, including lists inside lists.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Creating a list and indexing
    Items are separated by commas. Like in strings, the first item has index 0.
    """)
    return


@app.cell
def _():
    numbers = [4, 2, 9, 1, 5, 6]
    print(numbers, type(numbers))
    print(len(numbers))

    print(numbers[0])
    print(numbers[1])
    print(numbers[2])
    print(numbers[3])
    print(numbers[4])
    print(numbers[5])

    return (numbers,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Negative indexing
    Negative indexes count from the end, so `-1` is the last item and `-6` is the first item of a six-item list.
    """)
    return


@app.cell
def _(numbers):
    print(numbers[-1])
    print(numbers[-2])
    print(numbers[-3])
    print(numbers[-4])
    print(numbers[-5])
    print(numbers[-6])

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Looping over a list
    You can loop over the positions with `range(len(...))`, or loop directly over the items.
    """)
    return


@app.cell
def _(numbers):
    for _i in range(len(numbers)):
        print(numbers[_i], end=" ")
    print()

    for _num in numbers:
        print(_num, end=" ")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Lists are mutable
    Unlike strings, a list can be changed after it is created by assigning to one of its positions.
    """)
    return


@app.cell
def _():
    scores = [4, 2, 9, 1, 5, 6]
    print(scores)
    scores[0] = 10
    print(scores)

    scores[2] = scores[2] * scores[1]
    print(scores)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Slicing
    Slicing works exactly like it does for strings: the result is a new list.
    """)
    return


@app.cell
def _(numbers):
    print(numbers[1:4])  # from index 1 to index 3
    print(numbers[2:])  # from index 2 to the end
    print(numbers[:4])  # from the start to index 3
    print(numbers[::2])  # every second item
    print(numbers[::-1])  # the whole list backwards

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Joining, repeating and checking membership
    `+` joins two lists, `*` repeats a list, and `in` checks whether an item is present.
    """)
    return


@app.cell
def _(numbers):
    print([1, 2, 3] + [4, 5])
    print([0] * 5)
    print(9 in numbers)
    print(100 in numbers)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Lists can hold any type
    A list can contain floats, strings or a mixture of types. `type()` shows what each item is.
    """)
    return


@app.cell
def _():
    _float_numbers = [4.5, 2.3, 9.1, 1.0, 5.6, 6.2]

    for _num in _float_numbers:
        print(_num, type(_num), "|", end=" ")

    return


@app.cell
def _():
    _string_list = ["apple", "banana", "cherry", "date"]

    for _fruit in _string_list:
        print(_fruit, type(_fruit), "|", end=" ")

    return


@app.cell
def _():
    mixed_list = [1, 2.5, "hello", True, 3 + 4j]

    for item in mixed_list:
        print(item, type(item), "|", end=" ")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Nested lists
    A list can contain other lists. Use one index for the inner list and a second index for the item inside it.
    """)
    return


@app.cell
def _():
    nested_list = [[1, 2], [3.5, 4.5], ["a", "b", "c"], [True, False], [5 + 6j, 7 + 8j]]

    for _sublist in nested_list:
        for _element in _sublist:
            print(_element, type(_element), "|", end=" ")
        print(_sublist, type(_sublist), "|", end="\n")

    print(nested_list[2][1])

    return


if __name__ == "__main__":
    app.run()
