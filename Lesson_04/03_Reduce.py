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
    # Reduce
    `reduce()` combines all the items of a collection into one single value by applying a function again and again. You will learn how it works step by step and use it for sums, maximums and products.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## `reduce()`
    `reduce()` lives in the `functools` module, so it has to be imported first. `reduce(function, iterable)` takes the first two items, passes them to the function, then passes that result together with the third item, and so on until one value is left. The function you give it must accept exactly two arguments, which is a perfect job for a lambda.
    """)
    return


@app.cell
def _():
    from functools import reduce

    lst = list(range(2, 34, 3))
    print(lst)

    summation = reduce(lambda x, y: x + y, lst)
    print(summation)

    return lst, reduce


@app.cell
def _(mo):
    mo.md(r"""
    ## Seeing the steps
    Here is what `reduce()` did for a short list `[1, 2, 3, 4]` with addition: `1 + 2 = 3`, then `3 + 3 = 6`, then `6 + 4 = 10`. We can print the steps by using a regular function instead of a lambda.
    """)
    return


@app.cell
def _(reduce):
    def add_verbose(x, y):
        print(f"{x} + {y} = {x + y}")
        return x + y


    print(reduce(add_verbose, [1, 2, 3, 4]))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Finding the maximum
    The function can hold any logic. Here it keeps the bigger of the two values, so after all the steps the biggest one remains.
    """)
    return


@app.cell
def _(lst, reduce):
    max_val = reduce(lambda x, y: x if x > y else y, lst)
    print(max_val)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Product and an initial value
    Multiplying everything together works the same way. `reduce()` also accepts an optional third argument, the **initial value**, which is used as the very first `x`. It is also what is returned for an empty list, so it avoids an error in that case.
    """)
    return


@app.cell
def _(reduce):
    numbers = [2, 3, 4, 5]
    print(reduce(lambda x, y: x * y, numbers))

    print(reduce(lambda x, y: x + y, numbers, 100))
    print(reduce(lambda x, y: x + y, [], 0))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Joining strings
    `reduce()` is not limited to numbers. Here it joins words into one sentence.
    """)
    return


@app.cell
def _(reduce):
    words = ["Python", "is", "fun"]
    sentence = reduce(lambda x, y: x + " " + y, words)
    print(sentence)

    return


if __name__ == "__main__":
    app.run()
