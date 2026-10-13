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
    # Seaborn Regression and Multi-Variable Plots
    You will fit a trend line through a scatter plot with regression plots, and then look at many columns at once with pair plots and joint plots.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import seaborn as sns
    from pathlib import Path

    student_df = pd.read_csv(Path(__file__).resolve().parent / "student_dataset_complete.csv")
    student_df

    return sns, student_df


@app.cell
def _(mo):
    mo.md(r"""
    ## Regression Plot
    `sns.regplot()` draws a scatter plot together with a fitted straight line that shows the trend. The shaded band is the confidence interval of the line.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.regplot(data=student_df, x="study_hours", y="test_score")

    return


@app.cell
def _(mo):
    mo.md(r"""
    `sns.lmplot()` is the figure-level version. It can draw a separate trend line for each `hue` group.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.lmplot(data=student_df, x="study_hours", y="test_score")

    return


@app.cell
def _(sns, student_df):
    sns.lmplot(data=student_df, x="study_hours", y="test_score", hue="gender")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Pair Plot
    `sns.pairplot()` draws every numeric column against every other column. We first select only a few columns to keep the grid small.
    """)
    return


@app.cell
def _(student_df):
    student_marks = student_df[
        ["attendance_rate", "study_hours", "gender", "Marks"]
    ]
    student_marks

    return (student_marks,)


@app.cell
def _(sns, student_marks):
    sns.pairplot(data=student_marks)

    return


@app.cell
def _(mo):
    mo.md(r"""
    The `kind` argument changes the type of the off-diagonal plots, for example to histograms (`"hist"`) or regression plots (`"reg"`).
    """)
    return


@app.cell
def _(sns, student_marks):
    sns.pairplot(data=student_marks, kind="hist")

    return


@app.cell
def _(sns, student_marks):
    sns.pairplot(data=student_marks, kind="reg")

    return


@app.cell
def _(mo):
    mo.md(r"""
    With `hue` the points of each group get their own color.
    """)
    return


@app.cell
def _(sns, student_marks):
    sns.pairplot(data=student_marks, hue="gender")

    return


@app.cell
def _(sns, student_marks):
    sns.pairplot(data=student_marks, hue="gender", kind="reg")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Joint Plot
    `sns.jointplot()` shows the relation of two columns in the center and the distribution of each column on the sides.
    """)
    return


@app.cell
def _(sns, student_df):
    sns.jointplot(data=student_df, x="study_hours", y="Marks")

    return


@app.cell
def _(sns, student_df):
    sns.jointplot(data=student_df, x="study_hours", y="Marks", kind="kde")

    return


@app.cell
def _(sns, student_df):
    sns.jointplot(
        data=student_df, x="study_hours", y="Marks", kind="kde", hue="gender"
    )

    return


if __name__ == "__main__":
    app.run()
