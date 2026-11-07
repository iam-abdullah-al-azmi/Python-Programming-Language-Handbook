import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="NumPy Operations")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sorting, Searching and Comparing Arrays
    Learn how to compare arrays, sort them, find the positions of values with `where`, `argmax` and `argmin`, and count the values that match a condition.
    """)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Comparison
    A comparison between arrays gives a boolean array. `np.all` is True when every element is True and `np.any` is True when at least one element is True.
    """)
    return


@app.cell
def _(np):
    array_a = np.array([[1, 4, 9, 16, 25], [1, 4, 9, 16, 25]])
    array_b = np.array([[26, 29, 34, 41, 50], [11, 14, 19, 26, 35]])
    print(array_a)
    print(array_b > array_a)
    print(np.all(array_b > array_a))
    print(np.any(array_b > array_a))
    print(np.all(array_b > 30), np.any(array_b > 30))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Sorting
    - `arr.sort()` sorts the array in place (the original changes)
    - `np.sort(arr)` returns a sorted copy and leaves the original alone
    - for a 2D array there are two possibilities: `axis=1` sorts every row (horizontal) and `axis=0` sorts every column (vertical)
    """)
    return


@app.cell
def _(np):
    np.random.seed(3)
    array_five = np.random.randint(1, 10, size=10)
    print(array_five)
    array_five.sort()  # in place sorting
    print(array_five)

    array_six = np.random.randint(1, 10, size=10)
    print(array_six)
    array_sort = np.sort(array_six)  # copying then sorting
    print(array_sort)
    print(array_six)
    return


@app.cell
def _(np):
    array_four_1 = np.array([[3, 2, 8, 5], [45, 23, 9, 32]])
    two_dim_horizontal_sort = np.sort(array_four_1, axis=1)
    print(two_dim_horizontal_sort)
    two_dim_vertical_sort = np.sort(array_four_1, axis=0)
    print(two_dim_vertical_sort)

    return (array_four_1,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Searching
    `np.where(condition)` returns the positions where the condition is True. `np.where(condition, x, y)` picks `x` where the condition is True and `y` otherwise.
    `np.argmax` and `np.argmin` return the position of the largest and the smallest value (counted in the flattened array).
    """)
    return


@app.cell
def _(array_four_1, np):
    print(array_four_1)
    index = np.where(array_four_1 == 8)
    print(index)
    index = np.where(array_four_1 > 8)
    print(index)
    index = np.where(array_four_1 > 8, array_four_1, 0)
    print(index)
    max_val = np.argmax(array_four_1)
    print(max_val)
    min_val = np.argmin(array_four_1)
    print(min_val)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Counting
    `np.count_nonzero` counts the True values of a condition.
    """)
    return


@app.cell
def _(np):
    np.random.seed(5)
    array_seven = np.random.randint(1, 100, 100)
    print(array_seven)

    no_greater_than_forty = np.count_nonzero(array_seven > 40)
    print(no_greater_than_forty)
    return


if __name__ == "__main__":
    app.run()
