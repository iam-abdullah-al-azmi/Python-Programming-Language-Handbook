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
    # List Methods and Sorting
    List methods are built-in tools that add, remove, find and reorder items. You will learn the common methods, how to sort a list, and how a list can behave like a stack or a queue.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Adding items
    `append()` adds an item at the end, `insert(index, item)` puts it at a given position and shifts the rest to the right, and `extend()` adds all the items of another list.
    """)
    return


@app.cell
def _():
    numbers = [4, 2, 9, 1, 5, 6]

    numbers.append(20)
    print(numbers)

    numbers.insert(2, 15)  # insert 15 at index 2, the rest shifts to the right
    print(numbers)

    numbers.extend([7, 8])
    print(numbers)

    return (numbers,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Removing items
    `pop()` removes the last item (or the item at a given index) and returns it. `remove(value)` removes the first occurrence of a value. `del` removes by index, and `clear()` empties the list.
    """)
    return


@app.cell
def _(numbers):
    numbers.pop()  # removes the last element
    print(numbers)

    numbers.pop(2)  # removes the element at index 2
    print(numbers)

    numbers.remove(5)  # removes the first occurrence of 5
    print(numbers)

    del numbers[0]
    print(numbers)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Searching and counting
    `index()` gives the position of the first match, and `count()` says how many times a value occurs.
    """)
    return


@app.cell
def _():
    letters = ["a", "b", "c", "b", "a", "b"]
    print(letters.index("c"))
    print(letters.count("b"))
    print(len(letters))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Sorting
    `sort()` rearranges the list itself in ascending order. `sort(reverse=True)` sorts in descending order, and `reverse()` simply flips the current order. Strings are sorted alphabetically.
    """)
    return


@app.cell
def _():
    sort_numbers = [4, 2, 9, 1, 5, 6]
    sort_floats = [4.5, 2.3, 9.1, 1.0, 5.6, 6.2]
    sort_strings = ["cherry", "apple", "date", "banana"]

    sort_numbers.sort()  # smallest to largest
    sort_floats.sort()
    sort_strings.sort()  # alphabetical order

    print(f"Sorted numbers: {sort_numbers} | Sorted floats: {sort_floats} | Sorted strings: {sort_strings}")

    sort_numbers.sort(reverse=True)  # largest to smallest
    print(sort_numbers)

    sort_numbers.reverse()  # flips the current order
    print(sort_numbers)

    return


@app.cell
def _(mo):
    mo.md(r"""
    A list with mixed types cannot be sorted because Python does not know how to compare, for example, a string with a float. `[1, 2.5, "hello"].sort()` raises a `TypeError`, and so does sorting a list of lists that hold different kinds of items.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## `sort()` versus `sorted()`
    `sort()` changes the list in place and returns `None`. The built-in `sorted()` function leaves the original untouched and gives back a new sorted list. Both accept `reverse=True` and a `key` function, such as `len` to sort words by length.
    """)
    return


@app.cell
def _():
    original = [3, 1, 2]
    new_list = sorted(original)
    print(original, new_list)

    words = ["banana", "fig", "cherry", "kiwi"]
    print(sorted(words, key=len))
    print(sorted(words, key=len, reverse=True))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Copying a list
    Writing `b = a` does not copy a list: both names refer to the same list. Use `copy()` (or a full slice `a[:]`) to make an independent copy.
    """)
    return


@app.cell
def _():
    a = [1, 2, 3]
    b = a
    c = a.copy()

    a.append(4)
    print(a, b, c)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Stack as a list
    A stack works like plates placed one above another. The last plate placed is the first one taken (last in, first out). `append()` pushes and `pop()` removes from the top.
    """)
    return


@app.cell
def _():
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)

    print(stack)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Queue as a list
    In a queue the first element that comes in is the first one to go out (first in, first out), like a line of people waiting to buy a ticket. We add at the end with `append()` and remove from the front with `pop(0)`.
    """)
    return


@app.cell
def _():
    queue = []

    # insertion
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)

    # remove
    print(f"removed element: {queue.pop(0)}")

    # accessing the front element
    print(f"front element: {queue[0]}")

    # length of the queue
    print(f"length of queue: {len(queue)}")

    # last element
    print(f"last element: {queue[-1]}")

    print(f"removed element: {queue.pop(0)}")
    print(f"removed element: {queue.pop(0)}")
    print(f"removed element: {queue.pop(0)}")
    print(f"removed element: {queue.pop(0)}")

    return


if __name__ == "__main__":
    app.run()
