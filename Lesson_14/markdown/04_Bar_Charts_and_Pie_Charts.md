---
title: Matplotlib Visualization
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Bar Charts and Pie Charts
You will group a dataset by a category, count the rows in each group, and show the counts as a bar chart and as a pie chart with percentages and an exploded slice.
<!---->
## Reading the Data
The IPL 2022 dataset lists every player together with the team that bought them.

```python {.marimo}
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ipl_df = pd.read_csv(Path(__file__).resolve().parent / "ipl_2022_dataset.csv")
ipl_df
```

## Counting Players per Team
Grouping by `Team` and taking the `size()` gives the number of players of each team. The group names form the index and the counts are the values.

```python {.marimo}
team_group = ipl_df.groupby("Team").size()
team_group
```

```python {.marimo}
print(team_group.index)
team_group.values
```

## Bar Chart
`plt.bar(names, heights)` draws one bar per category.

```python {.marimo}
plt.bar(team_group.index, team_group.values)
plt.gca()
```

## Pie Chart
`plt.pie()` shows each category as a share of the whole. The `labels` argument names the slices.

```python {.marimo}
plt.pie(team_group, labels=team_group.index)
plt.gca()
```

## Showing Percentages
`autopct` prints the percentage of each slice using a format string.

```python {.marimo}
plt.pie(team_group, labels=team_group.index, autopct="%1.1f%%")
plt.gca()
```

## Exploding a Slice
`explode` takes one number per slice; a value above zero pulls that slice away from the center.

```python {.marimo}
plt.pie(
    team_group,
    labels=team_group.index,
    autopct="%1.1f%%",
    explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1),
)
plt.gca()
```

## Adding a Shadow
`shadow=True` draws a shadow under the pie.

```python {.marimo}
plt.pie(
    team_group,
    labels=team_group.index,
    autopct="%1.1f%%",
    explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1),
    shadow=True,
)
plt.gca()
```

## Changing the Size
`radius` makes the pie bigger or smaller.

```python {.marimo}
plt.pie(
    team_group,
    labels=team_group.index,
    autopct="%1.1f%%",
    explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1),
    shadow=True,
    radius=1.5,
)
plt.gca()
```