import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Matplotlib Visualization")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Line Plots with Titles and Labels
    In this notebook you will draw your first Matplotlib line plots, give them a title and axis labels, and put two lines on the same chart.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Importing Matplotlib
    Matplotlib is Python's most popular plotting library. Its `pyplot` module is imported as `plt` by convention. We also use NumPy to create some sample data.
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    return np, plt


@app.cell
def _(mo):
    mo.md(r"""
    ## Creating Some Data
    We create the number of hours a student studied on each of ten days. A seed is used so that the random numbers are the same every time.
    """)
    return


@app.cell
def _(np):
    np.random.seed(42)

    hours_one = np.random.randint(2, 20, size=10)
    days = np.linspace(1, 10, 10, retstep=False, dtype="int64")
    hours_one

    return days, hours_one


@app.cell
def _(mo):
    mo.md(r"""
    ## A Simple Line Plot
    `plt.plot(x, y)` draws a line through the points. `plt.title()` adds a title, and `plt.xlabel()` and `plt.ylabel()` label the two axes. The last line `plt.gca()` returns the current plot so that the figure is displayed below the cell.
    """)
    return


@app.cell
def _(days, hours_one, plt):
    plt.title("Study Hours vs Days")
    plt.xlabel("Days")
    plt.ylabel("Study Hours")
    plt.plot(days, hours_one)
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Plotting Two Lines Together
    Calling `plt.plot()` more than once in the same cell draws all the lines on the same chart. Here a second student's study hours are added.
    """)
    return


@app.cell
def _(np):
    hours_two = np.random.randint(3, 30, size=10)
    hours_two

    return (hours_two,)


@app.cell
def _(days, hours_one, hours_two, plt):
    plt.title("Study Hours vs Days")
    plt.xlabel("Days")
    plt.ylabel("Study Hours")
    plt.plot(days, hours_one)
    plt.plot(days, hours_two)
    plt.gca()

    return


if __name__ == "__main__":
    app.run()
