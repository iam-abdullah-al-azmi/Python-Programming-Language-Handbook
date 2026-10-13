import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Fundamental")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 04: Run a sequence of list commands (insert, append, remove, sort, pop, reverse, print) on an empty list.
    """)
    return


@app.cell
def _():
    commands = ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1", "sort", "print", "pop", "reverse", "print"]
    lst = []
    for command in commands:
        parts = command.split()
        name = parts[0]
        args = [int(x) for x in parts[1:]]
        if name == "insert":
            lst.insert(args[0], args[1])
        elif name == "append":
            lst.append(args[0])
        elif name == "remove":
            lst.remove(args[0])
        elif name == "sort":
            lst.sort()
        elif name == "pop":
            lst.pop()
        elif name == "reverse":
            lst.reverse()
        elif name == "print":
            print(lst)
    return


if __name__ == "__main__":
    app.run()
