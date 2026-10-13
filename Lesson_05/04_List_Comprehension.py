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
    # List Comprehension
    A list comprehension builds a new list in a single line, replacing a loop that fills a list with `append()`. You will learn the general syntax, how to add a condition, and how to combine several loops.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## The loop version
    Collecting the even numbers from 1 to 20 with a normal loop takes four lines.
    """)
    return


@app.cell
def _():
    even = []

    for _i in range(1, 21):
        if _i % 2 == 0:
            even.append(_i)

    print(even)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## The comprehension version
    The general syntax is `[expression for item in iterable if condition]`. The `if` part is optional. The same result as above now fits in one line.
    """)
    return


@app.cell
def _():
    even_comp = [_i for _i in range(1, 21) if _i % 2 == 0]
    print(even_comp)

    random_list = [x**2 for x in range(10) if x % 2 == 0]
    print(random_list)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Transforming every item
    Without a condition, a comprehension transforms every item, which is like `map()`. Here each fruit name is capitalized with a loop, and then upper cased with a comprehension.
    """)
    return


@app.cell
def _():
    fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    capitalize_fruits = []

    for _fruit in fruits:
        capitalize_fruits.append(_fruit.capitalize())

    print(capitalize_fruits)

    upper_fruits = [_fruit.upper() for _fruit in fruits]
    print(upper_fruits)

    return (fruits,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Filtering with a condition
    Adding an `if` at the end keeps only the matching items, which is like `filter()`.
    """)
    return


@app.cell
def _(fruits):
    long_fruits = [_fruit for _fruit in fruits if len(_fruit) > 5]
    print(long_fruits)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## `if` / `else` inside the expression
    To choose between two results for every item, put the `if ... else ...` before the `for`.
    """)
    return


@app.cell
def _():
    labels = ["even" if _n % 2 == 0 else "odd" for _n in range(1, 8)]
    print(labels)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Nested loops in a comprehension
    A comprehension can have more than one `for`. They run like nested loops, with the first one as the outer loop. Here we build every combination `[a, b, c]` with `a` from 0 to 1, `b` from 0 to 2 and `c` from 0 to 1, first with loops and then with a comprehension, and finally with a condition that skips the combinations whose sum equals `n`.
    """)
    return


@app.cell
def _():
    x = 1
    y = 2
    z = 1
    n = 2

    for a in range(x + 1):
        for b in range(y + 1):
            for c in range(z + 1):
                print(a, b, c, end=" | ")

    lst = [[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1)]
    print(f"\n{lst}")

    lst = [[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n]
    print(lst)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Comprehension on a nested list
    A comprehension can also flatten a list of lists into one list.
    """)
    return


@app.cell
def _():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [value for row in matrix for value in row]
    print(flat)

    return


if __name__ == "__main__":
    app.run()
