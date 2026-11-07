import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Strings and Lists Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 03: Use a list as a queue: add three people to the line, then serve them one by one (first in, first out).
    """)
    return


@app.cell(hide_code=True)
def _():
    queue = []
    queue.append("Rafi")
    queue.append("Mim")
    queue.append("Sakib")
    print(f"Queue: {queue}")
    while len(queue) > 0:
        print(f"Serving: {queue.pop(0)} | Remaining: {queue}")

    return


if __name__ == "__main__":
    app.run()
