import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Tuples, Sets and Dictionaries")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Tuples
    A tuple is an ordered collection of values that cannot be changed after it is created. In this notebook you will create tuples, access their elements, unpack them and use their methods.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Creating a tuple
    A tuple is written with round brackets and can hold values of any type, even other tuples and lists.
    """)
    return


@app.cell
def _():
    int_tup = (10, 20, 30, 40, 50)
    print(f"Tuple: {int_tup} and its type is: {type(int_tup)}")

    float_tup = (10.5, 20.5, 30.5)
    print(f"Tuple: {float_tup} and its type is: {type(float_tup)}")

    mixed_tup = (10, 20.5, "Hello", [1, 2, 3], (4, 5))
    print(f"Tuple: {mixed_tup} and its type is: {type(mixed_tup)}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## A tuple with a single element
    If we just put a single value in parentheses, Python treats it as that value (an `int` here). To make it a tuple we need to add a comma after the value. We can also convert another sequence, such as a list, using the `tuple()` function.
    """)
    return


@app.cell
def _():
    not_a_tuple = (10)
    print(not_a_tuple, type(not_a_tuple))

    one_element_tup = (10,)
    print(one_element_tup, type(one_element_tup))

    from_list_tup = tuple([10, 20, 30])
    print(from_list_tup, type(from_list_tup))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Accessing tuple elements
    Like a list, a tuple supports indexing, negative indexing and slicing. A `for` loop can go through a tuple directly, without using `len()` or an index, because a tuple is iterable.
    """)
    return


@app.cell
def _():
    access_tup = (10, "mixed", 30.5, False, [1, 2, 3], (1, 2, 3))

    print(access_tup[0], access_tup[-1])  # first and last element
    print(access_tup[1:4])  # slicing returns a new tuple
    print(len(access_tup))

    for _item in access_tup:
        print(_item, type(_item), end=" | ")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Immutability
    A tuple cannot be changed after it is created, so assigning a new value to an element raises a `TypeError`. If we need a different tuple we have to build a new one.
    """)
    return


@app.cell
def _():
    frozen_tup = (10, 20, 30)
    try:
        frozen_tup[0] = 99
    except TypeError as error:
        print(f"TypeError: {error}")

    # build a new tuple instead
    new_tup = (99,) + frozen_tup[1:]
    print(new_tup)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Tuple unpacking
    We can assign the elements of a tuple to separate variables in a single statement. This also gives a neat way to swap or rotate values without a temporary variable.
    """)
    return


@app.cell
def _():
    point = (3, 4)
    x, y = point
    print(x, y)

    first, *rest = (1, 2, 3, 4)  # a starred name collects the remaining values
    print(first, rest)

    a, b, c = (5, 10, 15)
    a, b, c = (c, a, b)  # rotate the values
    print(a, b, c)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Tuple methods
    A tuple has only two methods, `count()` and `index()`, because it cannot be modified. Notice that `count()` only looks at the elements of the tuple itself, not inside the nested list or set.
    """)
    return


@app.cell
def _():
    method_tup = (10, 10, 24, 24, [10, 2, 3, 4], {10, 2, 3, 4})
    print(method_tup.count(10), method_tup.index(10))
    return


@app.cell
def _(mo):
    mo.md(r"""
    A function can call itself, so we can write `deep_count()` to count a value inside the nested containers as well.
    """)
    return


@app.cell
def _():
    def deep_count(sequence, target):
        count = 0
        for _item in sequence:
            if _item == target:
                count += 1
            elif isinstance(_item, (list, tuple, set)):
                count += deep_count(_item, target)
        return count


    deep_tup = (10, 10, 24, 24, [10, 2, 3, 4], {10, 2, 3, 4})
    print(deep_count(deep_tup, 10))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Hashing a tuple
    Because a tuple of immutable values never changes, it has a fixed `hash()` value. This is why tuples can be used as dictionary keys or set elements, while lists cannot.
    """)
    return


@app.cell
def _():
    integers = [1, 2]
    hash_tup = tuple(integers)
    print(f"Tuple: {hash_tup}")
    print(f"Hash: {hash(hash_tup)}")
    print(f"Same values, same hash: {hash(hash_tup) == hash((1, 2))}")
    return


if __name__ == "__main__":
    app.run()
