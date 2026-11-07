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
    # Styling Line Plots
    This notebook shows how to read data from a CSV file and make a line plot readable with a legend, colors, line width, line style, markers and a grid.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Reading the Data
    We use pandas to read the yearly enrollment of two courses from a CSV file. The path is built relative to this notebook.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent / "enrollment_data.csv")
    df

    return df, plt


@app.cell
def _(mo):
    mo.md(r"""
    ## Plotting Two Columns
    Each column of the DataFrame is plotted against the year. The `label` argument gives every line a name.
    """)
    return


@app.cell
def _(df, plt):
    plt.plot(df["Year"], df["Programming"], label="Programming")
    plt.plot(df["Year"], df["Digital Marketing"], label="Digital Marketing")
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Adding a Legend
    The labels are only shown when `plt.legend()` is called.
    """)
    return


@app.cell
def _(df, plt):
    plt.plot(df["Year"], df["Programming"], label="Programming")
    plt.plot(df["Year"], df["Digital Marketing"], label="Digital Marketing")

    plt.legend()
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Changing the Color
    The `color` argument accepts color names or hex codes.
    """)
    return


@app.cell
def _(df, plt):
    plt.plot(df["Year"], df["Programming"], label="Programming", color="#32a852")
    plt.plot(
        df["Year"],
        df["Digital Marketing"],
        label="Digital Marketing",
        color="#8b32a8",
    )

    plt.legend()
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Changing the Line Width
    The `linewidth` argument controls how thick a line is.
    """)
    return


@app.cell
def _(df, plt):
    plt.plot(
        df["Year"],
        df["Programming"],
        label="Programming",
        color="#32a852",
        linewidth=5,
    )
    plt.plot(
        df["Year"],
        df["Digital Marketing"],
        label="Digital Marketing",
        color="#8b32a8",
        linewidth=5,
    )

    plt.legend()
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Changing the Line Style
    The `linestyle` argument selects between solid, dashed (`"dashed"`), dash-dot (`"dashdot"`) and dotted (`"dotted"`) lines.
    """)
    return


@app.cell
def _(df, plt):
    plt.plot(
        df["Year"], df["Programming"], label="Programming", linestyle="dashdot"
    )
    plt.plot(
        df["Year"],
        df["Digital Marketing"],
        label="Digital Marketing",
        linestyle="dotted",
    )

    plt.legend()
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Adding Markers
    The `marker` argument marks every data point. `"o"` draws a circle.
    """)
    return


@app.cell
def _(df, plt):
    plt.plot(
        df["Year"],
        df["Programming"],
        label="Programming",
        linestyle="dashdot",
        marker="o",
    )
    plt.plot(
        df["Year"],
        df["Digital Marketing"],
        label="Digital Marketing",
        linestyle="dotted",
        marker="o",
    )

    plt.legend()
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Putting It All Together with a Grid
    `plt.grid()` draws grid lines behind the plot. Each line can have its own style, and passing `linewidth=None` simply keeps the default width.
    """)
    return


@app.cell
def _(df, plt):
    plt.plot(
        df["Year"],
        df["Programming"],
        label="Programming",
        linestyle="dashdot",
        marker="o",
        linewidth=3,
    )
    plt.plot(
        df["Year"],
        df["Digital Marketing"],
        label="Digital Marketing",
        linestyle="dotted",
        marker="o",
        linewidth=None,
    )

    plt.grid()
    plt.legend()
    plt.gca()

    return


if __name__ == "__main__":
    app.run()
