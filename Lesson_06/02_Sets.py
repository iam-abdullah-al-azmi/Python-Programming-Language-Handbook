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
    # Sets
    A set is a collection of unique, unordered elements. In this notebook you will create sets, add and remove elements and use set operations such as union, intersection and difference.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Creating a set
    A set is a built-in Python data structure that is mutable, stores unique elements and is unordered, so we cannot do indexing or slicing on it. Curly brackets with values make a set, but empty curly brackets make a dictionary, so an empty set must be created with `set()`.
    """)
    return


@app.cell
def _():
    A = {1, 2, 3}
    print(A, type(A))

    B = {}
    print(type(B))

    C = set()
    print(type(C))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Accessing elements
    Duplicates are removed automatically. We cannot ask for the element at an index, but we can loop over a set or test membership with `in`.
    """)
    return


@app.cell
def _():
    D = {1, 5, 4, 3, 2, 3, 2}
    print(D)  # no duplicate

    for _s in D:
        print(_s, end=" ")

    if 2 in D:
        print("\n2 is present")
    else:
        print("\nnot present")

    print(5 in D)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Adding elements
    `add()` inserts one element. Adding a value that is already present changes nothing. A set does not remember insertion order, so never rely on the position of an element.
    """)
    return


@app.cell
def _():
    E = {2, 3, 4, 4, 5, 6, 8, 8, 0, 10, 1, 2}
    print(E)

    E.add(4)  # already present, no duplicate
    print(E)

    E.add(7)
    print(E)

    E.add(-1)
    print(E)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Removing elements
    - `remove()` deletes the specified element (not an index) and raises a `KeyError` if it is missing.
    - `discard()` also deletes the element but stays silent if it is missing.
    - `pop()` removes and returns an arbitrary element, since sets are unordered and do not support indexing.
    """)
    return


@app.cell
def _():
    L = {3, 5, 6, 7}

    L.remove(5)
    print(L)

    L.discard(100)  # not present, no error
    print(L)

    popped = L.pop()
    print(f"Popped one element, {len(L)} left")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Union and intersection
    - `union()` returns a new set with the elements of all the sets.
    - `intersection()` returns a new set with the elements found in all the sets.
    - `isdisjoint()` tells whether two sets have no common element.
    """)
    return


@app.cell
def _():
    F = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    G = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
    I = {4, 3, 5, 6, 2, 6, 2, 4, 7, 5, 23, 24, 53}

    print(f"Union of F and G: {F.union(G)}")
    print(f"Union of F, G and I: {F.union(G).union(I)}")
    print(f"Intersection of F and G: {F.intersection(G)}")
    print(f"Intersection of F, G and I: {F.intersection(G).intersection(I)}")
    print(f"Union of I with Intersection of F and G: {F.intersection(G).union(I)}")
    print(F.isdisjoint(G))
    print({1, 2, 3}.isdisjoint({4, 5}))

    # the order of the sets does not matter for union and intersection
    print(G.union(F) == F.union(G), G.intersection(F) == F.intersection(G))
    return F, G


@app.cell
def _(mo):
    mo.md(r"""
    ## Subsets and supersets
    `issubset()` checks whether every element of a set is in another set, and `issuperset()` checks the opposite direction.
    """)
    return


@app.cell
def _(F, G):
    print(F.issubset(G))

    H = {1, 2, 3}
    J = {1, 2, 3, 4, 5}
    print(H.issubset(J))
    print(J.issubset(H))
    print(J.issuperset(H))
    print(H.issuperset(J))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Difference and symmetric difference
    - `difference()` returns a new set with the elements present in the original set but not in any of the given sets, that is the mathematical difference A - (B U C U ...). The original set is not modified.
    - `symmetric_difference()` (or the `^` operator) returns the elements that are in exactly one of the two sets.
    """)
    return


@app.cell
def _():
    P = {1, 2, 3, 4, 5, 6, 8, 10}
    Q = {2, 3, 4, 5, 7}
    R = {3, 5, 6, 7}
    # Q U R = {2, 3, 4, 5, 6, 7}, so P - (Q U R) = {1, 8, 10}
    print(P.difference(Q, R))

    M = {2, 3, 4, 5, 6, 7}
    N = {6, 7, 8, 9, 10}
    print(M ^ N)
    print(M.symmetric_difference(N))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Set operators and removing duplicates
    The operators `|`, `&` and `-` do the same job as `union()`, `intersection()` and `difference()`. Converting a list into a set is also the quickest way to remove its duplicate values.
    """)
    return


@app.cell
def _():
    S1 = {1, 2, 3, 4}
    S2 = {3, 4, 5, 6}
    print(S1 | S2, S1 & S2, S1 - S2)

    numbers = [3, 1, 2, 3, 4, 1, 5, 2, 5]
    print(sorted(set(numbers)))
    return


if __name__ == "__main__":
    app.run()
