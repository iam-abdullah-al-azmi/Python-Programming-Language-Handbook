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
    # Seaborn Line and Scatter Plots
    Seaborn is built on top of Matplotlib and works directly with DataFrames. In this notebook you will draw line plots and scatter plots, color and style the points by other columns, and split a chart into several panels.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Reading the Data
    Seaborn is imported as `sns`. The `sns_data.csv` file holds one row per student record with the study hours, test score, week, attendance rate and more.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import seaborn as sns
    from pathlib import Path

    df = pd.read_csv(Path(__file__).resolve().parent / "sns_data.csv")
    df

    return df, pd, sns, Path


@app.cell
def _(mo):
    mo.md(r"""
    ## Line Plot
    `sns.lineplot()` takes the DataFrame as `data` and the column names as `x` and `y`. When several rows share the same `x` value, Seaborn plots their average and draws a shaded band around it.
    """)
    return


@app.cell
def _(df, sns):
    sns.lineplot(data=df, x="week", y="attendance_rate")

    return


@app.cell
def _(mo):
    mo.md(r"""
    Setting `errorbar=None` removes the shaded band.
    """)
    return


@app.cell
def _(df, sns):
    sns.lineplot(data=df, x="week", y="attendance_rate", errorbar=None)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## One Line per Category with hue
    The `hue` argument draws a separate colored line for every value of a column.
    """)
    return


@app.cell
def _(df, sns):
    sns.lineplot(
        data=df, x="week", y="attendance_rate", hue="gender", errorbar=None
    )

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## relplot
    `sns.relplot()` is a more general function for "relational" plots. The `kind` argument selects a line plot or a scatter plot, and the other arguments are the same.
    """)
    return


@app.cell
def _(df, sns):
    sns.relplot(
        kind="line",
        data=df,
        x="week",
        y="attendance_rate",
        hue="gender",
        errorbar=None,
    )

    return


@app.cell
def _(df, sns):
    sns.relplot(
        kind="line",
        data=df,
        x="week",
        y="attendance_rate",
        hue="class_level",
        errorbar=None,
    )

    return


@app.cell
def _(df, sns):
    sns.relplot(
        kind="line",
        data=df,
        x="week",
        y="study_hours",
        hue="class_level",
        errorbar=None,
    )

    return


@app.cell
def _(df, sns):
    sns.relplot(
        kind="line",
        data=df,
        x="study_hours",
        y="test_score",
        hue="class_level",
        errorbar=None,
    )

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Scatter Plot
    `sns.scatterplot()` draws one dot per row. This is the quickest way to see whether two columns are related.
    """)
    return


@app.cell
def _(df, sns):
    sns.scatterplot(data=df, x="study_hours", y="test_score")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Coloring, Styling and Sizing the Dots
    `hue` colors the dots by a column, `style` changes the marker shape, and `size` changes the dot size. This way one chart can show up to five columns at once.
    """)
    return


@app.cell
def _(df, sns):
    sns.scatterplot(data=df, x="study_hours", y="test_score", hue="gender")

    return


@app.cell
def _(df, sns):
    sns.scatterplot(
        data=df, x="study_hours", y="test_score", hue="gender", style="class_level"
    )

    return


@app.cell
def _(df, sns):
    sns.scatterplot(
        data=df, x="study_hours", y="test_score", hue="gender", style="subject"
    )

    return


@app.cell
def _(df, sns):
    sns.scatterplot(
        data=df,
        x="study_hours",
        y="test_score",
        hue="gender",
        style="subject",
        size="Tshirt_size",
    )

    return


@app.cell
def _(df, sns):
    sns.relplot(
        kind="scatter",
        data=df,
        x="study_hours",
        y="test_score",
        hue="gender",
        style="subject",
        size="Tshirt_size",
    )

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Built-in Example Datasets
    Seaborn can load small example datasets by name with `sns.load_dataset()`. The first time it needs an internet connection to download the data. The `tips` dataset records restaurant bills and tips.
    """)
    return


@app.cell
def _(sns):
    tips_data = sns.load_dataset("tips")
    tips_data

    return (tips_data,)


@app.cell
def _(sns, tips_data):
    sns.relplot(kind="scatter", data=tips_data, x="total_bill", y="tip")

    return


@app.cell
def _(sns, tips_data):
    sns.relplot(kind="scatter", data=tips_data, x="total_bill", y="tip", hue="sex")

    return


@app.cell
def _(sns, tips_data):
    sns.relplot(
        kind="scatter",
        data=tips_data,
        x="total_bill",
        y="tip",
        hue="sex",
        style="time",
    )

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Splitting a Chart into Panels
    A larger dataset with more columns is used for the rest of this notebook. Only `relplot()` (and the other figure-level functions) can split a chart into several panels, using `col` for columns and `row` for rows.
    """)
    return


@app.cell
def _(Path, pd):
    student_df = pd.read_csv(Path(__file__).resolve().parent / "student_dataset_complete.csv")
    student_df

    return (student_df,)


@app.cell
def _(sns, student_df):
    sns.scatterplot(data=student_df, x="study_hours", y="test_score")

    return


@app.cell
def _(sns, student_df):
    sns.scatterplot(data=student_df, x="study_hours", y="test_score", hue="gender")

    return


@app.cell
def _(sns, student_df):
    sns.relplot(
        kind="scatter",
        data=student_df,
        x="study_hours",
        y="test_score",
        hue="gender",
    )

    return


@app.cell
def _(sns, student_df):
    sns.relplot(
        kind="scatter",
        data=student_df,
        x="study_hours",
        y="test_score",
        col="gender",
    )

    return


@app.cell
def _(sns, student_df):
    sns.relplot(
        kind="scatter",
        data=student_df,
        x="study_hours",
        y="test_score",
        col="gender",
        row="hostel",
    )

    return


@app.cell
def _(mo):
    mo.md(r"""
    `col_wrap` breaks a long row of panels into several lines.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.relplot(
        kind="scatter",
        data=student_df,
        x="study_hours",
        y="test_score",
        col="week",
    )

    return


@app.cell
def _(sns, student_df):
    sns.relplot(
        kind="scatter",
        data=student_df,
        x="study_hours",
        y="test_score",
        col="week",
        col_wrap=2,
    )

    return


if __name__ == "__main__":
    app.run()
