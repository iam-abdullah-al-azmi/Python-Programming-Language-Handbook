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
    # Bar Charts and Pie Charts
    You will group a dataset by a category, count the rows in each group, and show the counts as a bar chart and as a pie chart with percentages and an exploded slice.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Reading the Data
    The IPL 2022 dataset lists every player together with the team that bought them.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    ipl_df = pd.read_csv(Path(__file__).resolve().parent / "ipl_2022_dataset.csv")
    ipl_df

    return ipl_df, plt


@app.cell
def _(mo):
    mo.md(r"""
    ## Counting Players per Team
    Grouping by `Team` and taking the `size()` gives the number of players of each team. The group names form the index and the counts are the values.
    """)
    return


@app.cell
def _(ipl_df):
    team_group = ipl_df.groupby("Team").size()
    team_group

    return (team_group,)


@app.cell
def _(team_group):
    print(team_group.index)
    team_group.values

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Bar Chart
    `plt.bar(names, heights)` draws one bar per category.
    """)
    return


@app.cell
def _(plt, team_group):
    plt.bar(team_group.index, team_group.values)
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Pie Chart
    `plt.pie()` shows each category as a share of the whole. The `labels` argument names the slices.
    """)
    return


@app.cell
def _(plt, team_group):
    plt.pie(team_group, labels=team_group.index)
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Showing Percentages
    `autopct` prints the percentage of each slice using a format string.
    """)
    return


@app.cell
def _(plt, team_group):
    plt.pie(team_group, labels=team_group.index, autopct="%1.1f%%")
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exploding a Slice
    `explode` takes one number per slice; a value above zero pulls that slice away from the center.
    """)
    return


@app.cell
def _(plt, team_group):
    plt.pie(
        team_group,
        labels=team_group.index,
        autopct="%1.1f%%",
        explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1),
    )
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Adding a Shadow
    `shadow=True` draws a shadow under the pie.
    """)
    return


@app.cell
def _(plt, team_group):
    plt.pie(
        team_group,
        labels=team_group.index,
        autopct="%1.1f%%",
        explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1),
        shadow=True,
    )
    plt.gca()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Changing the Size
    `radius` makes the pie bigger or smaller.
    """)
    return


@app.cell
def _(plt, team_group):
    plt.pie(
        team_group,
        labels=team_group.index,
        autopct="%1.1f%%",
        explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1),
        shadow=True,
        radius=1.5,
    )
    plt.gca()

    return


if __name__ == "__main__":
    app.run()
