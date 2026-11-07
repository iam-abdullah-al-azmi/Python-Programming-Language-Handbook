---
title: Seaborn and Plotly Visualization
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Seaborn Distribution and Categorical Plots
In this notebook you will look at how the values of one column are distributed with histograms and KDE plots, and compare categories with count plots and bar plots.

```python {.marimo}
import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path

student_df = pd.read_csv(Path(__file__).resolve().parent / "student_dataset_complete.csv")
student_df
```

## Histogram
`sns.histplot()` counts how many values fall into each bin of a numeric column.

```python {.marimo}
sns.histplot(data=student_df, x="attendance_rate")
```

With `hue` the histograms of different groups are drawn on top of each other in different colors.

```python {.marimo}
sns.histplot(data=student_df, x="attendance_rate", hue="gender")
```

The `bins` argument sets the number of bins and `element="step"` draws only the outline of each histogram.

```python {.marimo}
sns.histplot(data=student_df, x="attendance_rate", hue="gender", bins=15)
```

```python {.marimo}
sns.histplot(
    data=student_df, x="attendance_rate", hue="gender", bins=10, element="step"
)
```

`sns.displot()` is the figure-level version, which can also split the plot into panels with `col`.

```python {.marimo}
sns.displot(kind="hist", data=student_df, x="attendance_rate", col="gender")
```

## KDE Plot
A KDE (Kernel Density Estimation) plot draws a smooth curve instead of bars to show how the values are distributed.

```python {.marimo}
sns.kdeplot(data=student_df, x="attendance_rate")
```

```python {.marimo}
sns.kdeplot(data=student_df, x="attendance_rate", hue="gender")
```

```python {.marimo}
sns.kdeplot(data=student_df, x="attendance_rate", hue="gender", fill=True)
```

## Count Plot
`sns.countplot()` counts the rows of every category of a column and shows the counts as bars.

```python {.marimo}
sns.countplot(data=student_df, x="gender")
```

```python {.marimo}
sns.countplot(data=student_df, x="subject", hue="gender")
```

## Bar Plot
`sns.barplot()` shows a numeric column for every category. By default each bar is the mean of the group, with an error bar showing the uncertainty.

```python {.marimo}
sns.barplot(data=student_df, x="gender", y="Marks")
```

`errorbar=None` removes the error bars, and `estimator` changes how each group is summarized, for example with the median or the maximum.

```python {.marimo}
sns.barplot(data=student_df, x="gender", y="Marks", errorbar=None)
```

```python {.marimo}
sns.barplot(
    data=student_df, x="gender", y="Marks", errorbar=None, estimator=np.median
)
```

```python {.marimo}
sns.barplot(
    data=student_df, x="gender", y="Marks", errorbar=None, estimator=np.max
)
```