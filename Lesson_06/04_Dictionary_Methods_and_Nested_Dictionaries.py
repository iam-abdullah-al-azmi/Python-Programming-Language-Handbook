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
    # Dictionary Methods and Nested Dictionaries
    This notebook covers the most useful dictionary methods, dictionary comprehensions and dictionaries that hold other dictionaries. You will learn how to build, merge and process dictionaries in a few lines.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## keys(), values() and items()
    These methods return view objects. A view is not a copy: it stays connected to the dictionary, so we do not have to call the method again after the dictionary changes. `items()` gives key-value pairs as tuples.
    """)
    return


@app.cell
def _():
    information_7 = dict(Name="Chem", System="Linux", Version=2.0, License="Apache")

    keys = information_7.keys()
    values = information_7.values()
    items = information_7.items()
    print(keys)
    print(values)
    print(items)

    information_7["Language"] = "Python"
    print(keys)  # updated automatically
    print(values)
    print(items)
    return


@app.cell
def _():
    information_8 = dict(Name="marimo", System="Linux", Version=1.0, License="GPL")
    item = information_8.items()

    print(item, type(item))

    for _i in item:
        print(_i, "|", type(_i))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## pop(), popitem() and clear()
    - `pop(key)` removes the given key and returns its value, so we must provide the key.
    - `popitem()` takes no argument and removes the last inserted key-value pair.
    - `clear()` removes every pair and leaves an empty dictionary.
    """)
    return


@app.cell
def _():
    squares = {1: 1, 2: 4, 3: 9, 4: 16}
    print(squares.pop(2))
    print(squares)

    print(squares.popitem())
    print(squares)

    squares.clear()
    print(squares)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## fromkeys(), setdefault() and copy()
    - `dict.fromkeys(keys, value)` builds a dictionary where every key gets the same value (`None` if none is given).
    - `setdefault(key, value)` returns the value of the key, and first inserts the key with the given value if it is missing.
    - `copy()` makes a separate (shallow) copy of a dictionary.
    """)
    return


@app.cell
def _():
    members = ("a", "b", "c", "d")
    print(dict.fromkeys(members))
    print(dict.fromkeys(members, "Code"))

    settings = {"theme": "dark"}
    print(settings.setdefault("theme", "light"))  # key exists, value is kept
    print(settings.setdefault("font", "mono"))  # key is added
    print(settings)

    original = {"a": 1}
    duplicate = original.copy()
    duplicate["a"] = 100
    print(original, duplicate)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Merging dictionaries
    `update()` merges another dictionary into the first one. The `|` operator builds a new merged dictionary instead. In both cases, if a key exists in both, the value from the second dictionary wins.
    """)
    return


@app.cell
def _():
    first = {"a": 1, "b": 2, "c": 3}
    second = {"c": 30, "d": 40}

    merged = first | second
    print(merged)
    print(first)  # unchanged

    first.update(second)
    print(first)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Dictionary comprehension
    Like a list comprehension, a dictionary comprehension builds a dictionary from a loop in one line, with an optional condition. `zip()` pairs the items of two sequences, which is handy for building a dictionary from two lists.
    """)
    return


@app.cell
def _():
    even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print(even_squares)

    # zip() creates the pairs (1, 1), (2, 2), ..., (10, 10) and only the pairs where k is even are kept,
    # that is why the keys are not 1, 2, 3, ...
    zipped_squares = {x: k**2 for x, k in zip(range(1, 11), range(1, 11)) if k % 2 == 0}
    print(zipped_squares)

    coordinates = [(10, 10.5), (20, 20.5), (30, 30.5)]
    locations = ["dhaka", "chattogram", "sylhet"]
    zone = {_key: _value for _key, _value in zip(coordinates, locations)}
    print(zone)
    return


@app.cell
def _(mo):
    mo.md(r"""
    With two nested loops the same key is produced many times, and each new value overwrites the old one, so only the last value of the inner loop is kept for every key.
    """)
    return


@app.cell
def _():
    overwritten = {_key: _val for _key in range(11) for _val in range(11)}
    print(overwritten)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Nested dictionaries
    The value of a key can itself be a dictionary. This is a natural way to store records, such as the details of several students. We read a nested value by chaining the keys, one pair of brackets for each level.
    """)
    return


@app.cell
def _():
    students = {
        "Rafi": {"age": 20, "marks": [80, 90, 70]},
        "Mim": {"age": 21, "marks": [95, 85, 100]},
    }

    print(students["Rafi"])
    print(students["Rafi"]["age"])
    print(students["Mim"]["marks"][0])
    return (students,)


@app.cell
def _(mo):
    mo.md(r"""
    We can change or add to an inner dictionary the same way as to a normal one, and loop through both levels with nested `for` loops.
    """)
    return


@app.cell
def _(students):
    students["Rafi"]["age"] = 22  # change an inner value
    students["Karim"] = {"age": 19, "marks": [60, 75, 80]}  # add a new record
    students["Mim"]["city"] = "Dhaka"  # add a new key to an inner dictionary

    for _name, _details in students.items():
        print(f"{_name}:")
        for _field, _value in _details.items():
            print(f"    {_field} -> {_value}")

    for _name, _details in students.items():
        average = sum(_details["marks"]) / len(_details["marks"])
        print(f"{_name}: average mark {average:.2f}")
    return


if __name__ == "__main__":
    app.run()
