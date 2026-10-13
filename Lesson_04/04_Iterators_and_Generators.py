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
    # Iterators and Generators
    An iterator hands out the items of a collection one at a time, and a generator is a simple way to create your own iterator with the `yield` keyword. You will learn how `iter()` and `next()` work and why generators are useful for large amounts of data.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Iterators with `iter()` and `next()`
    A list, a string or a `range` is an **iterable**: something you can loop over. `iter()` turns an iterable into an **iterator**, and each call to `next()` returns the following item.
    """)
    return


@app.cell
def _():
    fruits = ["apple", "banana", "cherry"]
    fruit_iterator = iter(fruits)

    print(type(fruit_iterator))
    print(next(fruit_iterator))
    print(next(fruit_iterator))
    print(next(fruit_iterator))

    return fruits, fruit_iterator


@app.cell
def _(mo):
    mo.md(r"""
    When the items run out, one more call to `next()` raises a `StopIteration` error, which signals that the iterator is exhausted. (Handling errors is covered in Lesson 09.)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## What a `for` loop does
    A `for` loop uses the very same mechanism behind the scenes: it calls `iter()` on the collection and then `next()` again and again until `StopIteration` appears. That is why a loop and manual `next()` calls visit the items in exactly the same order.
    """)
    return


@app.cell
def _():
    numbers_iterator = iter([10, 20, 30, 40])

    print(next(numbers_iterator), end="|")
    print(next(numbers_iterator), end="|")
    print(next(numbers_iterator), end="|")
    print(next(numbers_iterator))

    for _n in [10, 20, 30, 40]:
        print(_n, end="|")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Generators with `yield`
    A **generator function** looks like a normal function, but it uses `yield` instead of `return`. Calling it does not run the body. It gives you a generator object, which is an iterator. Each `next()` runs the body until the next `yield`, hands out that value and then pauses, remembering where it stopped.
    """)
    return


@app.cell
def _():
    def count_to_three():
        print("start")
        yield 1
        print("middle")
        yield 2
        print("end")
        yield 3


    counter = count_to_three()
    print(type(counter))
    print(next(counter))
    print(next(counter))
    print(next(counter))

    return


@app.cell
def _(mo):
    mo.md(r"""
    A generator can also be used in a `for` loop, which calls `next()` for you and stops cleanly at the end.
    """)
    return


@app.cell
def _():
    def even_numbers(limit):
        for number in range(2, limit + 1, 2):
            yield number


    for _even in even_numbers(10):
        print(_even, end=" ")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Why generators matter: data in chunks
    When we work with a huge dataset such as 100 GB or 100 TB, the computer memory (RAM) gets stuck if we try to load all of it at the same time. That is why the data is divided into chunks and processed one chunk at a time. A generator is perfect for this because it produces one chunk per `next()` and never holds everything in memory.
    """)
    return


@app.cell
def _():
    dataset = []
    for _x in range(1000):
        if _x % 3 != 0:
            dataset.append(_x**2)


    def data_loader(chunk_size, data):
        """Yield the data one chunk at a time.

        Args:
            chunk_size (int): size of each chunk
            data (list): the whole dataset
        """
        for i in range(0, len(data), chunk_size):
            yield data[i : i + chunk_size]


    chunks = data_loader(5, dataset)
    print(type(chunks))
    print(next(chunks))
    print(next(chunks))
    print(next(chunks))
    print(next(chunks))
    print(next(chunks))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## A generator can be endless
    A generator only does work when a value is requested, so it can even describe an infinite sequence. We simply take as many values as we need.
    """)
    return


@app.cell
def _():
    def natural_numbers():
        n = 1
        while True:
            yield n
            n += 1


    naturals = natural_numbers()
    for _ in range(5):
        print(next(naturals), end=" ")

    return


if __name__ == "__main__":
    app.run()
