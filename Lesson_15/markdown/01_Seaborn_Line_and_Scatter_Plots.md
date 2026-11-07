---
title: Seaborn and Plotly Visualization
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Seaborn Line and Scatter Plots
Seaborn is built on top of Matplotlib and works directly with DataFrames. In this notebook you will draw line plots and scatter plots, color and style the points by other columns, and split a chart into several panels.
<!---->
## Reading the Data
Seaborn is imported as `sns`. The `sns_data.csv` file holds one row per student record with the study hours, test score, week, attendance rate and more.

```python {.marimo}
import pandas as pd
import seaborn as sns
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent / "sns_data.csv")
df
```

## Line Plot
`sns.lineplot()` takes the DataFrame as `data` and the column names as `x` and `y`. When several rows share the same `x` value, Seaborn plots their average and draws a shaded band around it.

```python {.marimo}
sns.lineplot(data=df, x="week", y="attendance_rate")
```

Setting `errorbar=None` removes the shaded band.

```python {.marimo}
sns.lineplot(data=df, x="week", y="attendance_rate", errorbar=None)
```

## One Line per Category with hue
The `hue` argument draws a separate colored line for every value of a column.

```python {.marimo}
sns.lineplot(
    data=df, x="week", y="attendance_rate", hue="gender", errorbar=None
)
```

## relplot
`sns.relplot()` is a more general function for "relational" plots. The `kind` argument selects a line plot or a scatter plot, and the other arguments are the same.

```python {.marimo}
sns.relplot(
    kind="line",
    data=df,
    x="week",
    y="attendance_rate",
    hue="gender",
    errorbar=None,
)
```

```python {.marimo}
sns.relplot(
    kind="line",
    data=df,
    x="week",
    y="attendance_rate",
    hue="class_level",
    errorbar=None,
)
```

```python {.marimo}
sns.relplot(
    kind="line",
    data=df,
    x="week",
    y="study_hours",
    hue="class_level",
    errorbar=None,
)
```

```python {.marimo}
sns.relplot(
    kind="line",
    data=df,
    x="study_hours",
    y="test_score",
    hue="class_level",
    errorbar=None,
)
```

## Scatter Plot
`sns.scatterplot()` draws one dot per row. This is the quickest way to see whether two columns are related.

```python {.marimo}
sns.scatterplot(data=df, x="study_hours", y="test_score")
```

## Coloring, Styling and Sizing the Dots
`hue` colors the dots by a column, `style` changes the marker shape, and `size` changes the dot size. This way one chart can show up to five columns at once.

```python {.marimo}
sns.scatterplot(data=df, x="study_hours", y="test_score", hue="gender")
```

```python {.marimo}
sns.scatterplot(
    data=df, x="study_hours", y="test_score", hue="gender", style="class_level"
)
```

```python {.marimo}
sns.scatterplot(
    data=df, x="study_hours", y="test_score", hue="gender", style="subject"
)
```

```python {.marimo}
sns.scatterplot(
    data=df,
    x="study_hours",
    y="test_score",
    hue="gender",
    style="subject",
    size="Tshirt_size",
)
```

```python {.marimo}
sns.relplot(
    kind="scatter",
    data=df,
    x="study_hours",
    y="test_score",
    hue="gender",
    style="subject",
    size="Tshirt_size",
)
```

## Built-in Example Datasets
Seaborn can load small example datasets by name with `sns.load_dataset()`. The first time it needs an internet connection to download the data. The `tips` dataset records restaurant bills and tips.

```python {.marimo}
tips_data = sns.load_dataset("tips")
tips_data
```

```python {.marimo}
sns.relplot(kind="scatter", data=tips_data, x="total_bill", y="tip")
```

```python {.marimo}
sns.relplot(kind="scatter", data=tips_data, x="total_bill", y="tip", hue="sex")
```

```python {.marimo}
sns.relplot(
    kind="scatter",
    data=tips_data,
    x="total_bill",
    y="tip",
    hue="sex",
    style="time",
)
```

## Splitting a Chart into Panels
A larger dataset with more columns is used for the rest of this notebook. Only `relplot()` (and the other figure-level functions) can split a chart into several panels, using `col` for columns and `row` for rows.

```python {.marimo}
student_df = pd.read_csv(Path(__file__).resolve().parent / "student_dataset_complete.csv")
student_df
```

```python {.marimo}
sns.scatterplot(data=student_df, x="study_hours", y="test_score")
```

```python {.marimo}
sns.scatterplot(data=student_df, x="study_hours", y="test_score", hue="gender")
```

```python {.marimo}
sns.relplot(
    kind="scatter",
    data=student_df,
    x="study_hours",
    y="test_score",
    hue="gender",
)
```

```python {.marimo}
sns.relplot(
    kind="scatter",
    data=student_df,
    x="study_hours",
    y="test_score",
    col="gender",
)
```

```python {.marimo}
sns.relplot(
    kind="scatter",
    data=student_df,
    x="study_hours",
    y="test_score",
    col="gender",
    row="hostel",
)
```

`col_wrap` breaks a long row of panels into several lines.

```python {.marimo}
sns.relplot(
    kind="scatter",
    data=student_df,
    x="study_hours",
    y="test_score",
    col="week",
)
```

```python {.marimo}
sns.relplot(
    kind="scatter",
    data=student_df,
    x="study_hours",
    y="test_score",
    col="week",
    col_wrap=2,
)
```