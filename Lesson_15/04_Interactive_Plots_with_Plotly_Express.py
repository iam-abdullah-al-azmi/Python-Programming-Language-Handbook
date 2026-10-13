import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Seaborn and Plotly Visualization")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Interactive Plots with Plotly Express
    Plotly Express creates interactive charts that you can hover over, zoom into and pan. In this notebook you will draw scatter plots, a line plot and histograms with it.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Reading the Data
    Plotly Express is imported as `px`. Like Seaborn, it takes a DataFrame and the names of its columns.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import plotly.express as px
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent / "sns_data.csv")
    df

    return df, px


@app.cell
def _(mo):
    mo.md(r"""
    ## Scatter Plot
    `px.scatter()` returns a figure. Put it on the last line of the cell to display it, then hover over a dot to see its values.
    """)
    return


@app.cell
def _(df, px):
    px.scatter(data_frame=df, x="study_hours", y="test_score")

    return


@app.cell
def _(mo):
    mo.md(r"""
    The `color` argument colors the dots by a column.
    """)
    return


@app.cell
def _(df, px):
    px.scatter(data_frame=df, x="study_hours", y="test_score", color="gender")

    return


@app.cell
def _(mo):
    mo.md(r"""
    `size` changes the dot size by a column and `hover_data` adds more columns to the hover box.
    """)
    return


@app.cell
def _(df, px):
    px.scatter(
        data_frame=df,
        x="study_hours",
        y="test_score",
        color="gender",
        size="Tshirt_size",
        hover_data=["hostel", "subject"],
    )

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Line Plot
    `px.line()` connects the points in the order of the rows.
    """)
    return


@app.cell
def _(df, px):
    px.line(data_frame=df, x="study_hours", y="test_score")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Histogram
    `px.histogram()` counts the values of a column in bins.
    """)
    return


@app.cell
def _(df, px):
    px.histogram(data_frame=df, x="attendance_rate")

    return


@app.cell
def _(mo):
    mo.md(r"""
    With `color` the histograms of different groups are shown in different colors.
    """)
    return


@app.cell
def _(df, px):
    px.histogram(data_frame=df, x="attendance_rate", color="gender")

    return


@app.cell
def _(mo):
    mo.md(r"""
    For a text column, the histogram counts how often each category appears.
    """)
    return


@app.cell
def _(df, px):
    px.histogram(data_frame=df, x="class_level", color="gender")

    return


if __name__ == "__main__":
    app.run()
