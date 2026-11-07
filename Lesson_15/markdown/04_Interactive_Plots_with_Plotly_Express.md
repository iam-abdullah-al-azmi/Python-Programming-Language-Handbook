---
title: Seaborn and Plotly Visualization
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Interactive Plots with Plotly Express
Plotly Express creates interactive charts that you can hover over, zoom into and pan. In this notebook you will draw scatter plots, a line plot and histograms with it.
<!---->
## Reading the Data
Plotly Express is imported as `px`. Like Seaborn, it takes a DataFrame and the names of its columns.

```python {.marimo}
import pandas as pd
import plotly.express as px
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent / "sns_data.csv")
df
```

## Scatter Plot
`px.scatter()` returns a figure. Put it on the last line of the cell to display it, then hover over a dot to see its values.

```python {.marimo}
px.scatter(data_frame=df, x="study_hours", y="test_score")
```

The `color` argument colors the dots by a column.

```python {.marimo}
px.scatter(data_frame=df, x="study_hours", y="test_score", color="gender")
```

`size` changes the dot size by a column and `hover_data` adds more columns to the hover box.

```python {.marimo}
px.scatter(
    data_frame=df,
    x="study_hours",
    y="test_score",
    color="gender",
    size="Tshirt_size",
    hover_data=["hostel", "subject"],
)
```

## Line Plot
`px.line()` connects the points in the order of the rows.

```python {.marimo}
px.line(data_frame=df, x="study_hours", y="test_score")
```

## Histogram
`px.histogram()` counts the values of a column in bins.

```python {.marimo}
px.histogram(data_frame=df, x="attendance_rate")
```

With `color` the histograms of different groups are shown in different colors.

```python {.marimo}
px.histogram(data_frame=df, x="attendance_rate", color="gender")
```

For a text column, the histogram counts how often each category appears.

```python {.marimo}
px.histogram(data_frame=df, x="class_level", color="gender")
```