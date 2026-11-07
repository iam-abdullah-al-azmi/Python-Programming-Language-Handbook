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
    # Seaborn Distribution and Categorical Plots
    In this notebook you will look at how the values of one column are distributed with histograms and KDE plots, and compare categories with count plots and bar plots.
    """)
    return


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    from pathlib import Path

    student_df = pd.read_csv(Path(__file__).resolve().parent / "student_dataset_complete.csv")
    student_df

    return np, sns, student_df


@app.cell
def _(mo):
    mo.md(r"""
    ## Histogram
    `sns.histplot()` counts how many values fall into each bin of a numeric column.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.histplot(data=student_df, x="attendance_rate")

    return


@app.cell
def _(mo):
    mo.md(r"""
    With `hue` the histograms of different groups are drawn on top of each other in different colors.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.histplot(data=student_df, x="attendance_rate", hue="gender")

    return


@app.cell
def _(mo):
    mo.md(r"""
    The `bins` argument sets the number of bins and `element="step"` draws only the outline of each histogram.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.histplot(data=student_df, x="attendance_rate", hue="gender", bins=15)

    return


@app.cell
def _(sns, student_df):
    sns.histplot(
        data=student_df, x="attendance_rate", hue="gender", bins=10, element="step"
    )

    return


@app.cell
def _(mo):
    mo.md(r"""
    `sns.displot()` is the figure-level version, which can also split the plot into panels with `col`.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.displot(kind="hist", data=student_df, x="attendance_rate", col="gender")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## KDE Plot
    A KDE (Kernel Density Estimation) plot draws a smooth curve instead of bars to show how the values are distributed.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.kdeplot(data=student_df, x="attendance_rate")

    return


@app.cell
def _(sns, student_df):
    sns.kdeplot(data=student_df, x="attendance_rate", hue="gender")

    return


@app.cell
def _(sns, student_df):
    sns.kdeplot(data=student_df, x="attendance_rate", hue="gender", fill=True)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Count Plot
    `sns.countplot()` counts the rows of every category of a column and shows the counts as bars.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.countplot(data=student_df, x="gender")

    return


@app.cell
def _(sns, student_df):
    sns.countplot(data=student_df, x="subject", hue="gender")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Bar Plot
    `sns.barplot()` shows a numeric column for every category. By default each bar is the mean of the group, with an error bar showing the uncertainty.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.barplot(data=student_df, x="gender", y="Marks")

    return


@app.cell
def _(mo):
    mo.md(r"""
    `errorbar=None` removes the error bars, and `estimator` changes how each group is summarized, for example with the median or the maximum.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.barplot(data=student_df, x="gender", y="Marks", errorbar=None)

    return


@app.cell
def _(np, sns, student_df):
    sns.barplot(
        data=student_df, x="gender", y="Marks", errorbar=None, estimator=np.median
    )

    return


@app.cell
def _(np, sns, student_df):
    sns.barplot(
        data=student_df, x="gender", y="Marks", errorbar=None, estimator=np.max
    )

    return


if __name__ == "__main__":
    app.run()
