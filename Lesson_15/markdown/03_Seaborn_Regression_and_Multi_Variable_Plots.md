---
title: Seaborn and Plotly Visualization
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Seaborn Regression and Multi-Variable Plots
You will fit a trend line through a scatter plot with regression plots, and then look at many columns at once with pair plots and joint plots.

```python {.marimo}
import pandas as pd
import seaborn as sns
from pathlib import Path

student_df = pd.read_csv(Path(__file__).resolve().parent / "student_dataset_complete.csv")
student_df
```

## Regression Plot
`sns.regplot()` draws a scatter plot together with a fitted straight line that shows the trend. The shaded band is the confidence interval of the line.

```python {.marimo}
sns.regplot(data=student_df, x="study_hours", y="test_score")
```

`sns.lmplot()` is the figure-level version. It can draw a separate trend line for each `hue` group.

```python {.marimo}
sns.lmplot(data=student_df, x="study_hours", y="test_score")
```

```python {.marimo}
sns.lmplot(data=student_df, x="study_hours", y="test_score", hue="gender")
```

## Pair Plot
`sns.pairplot()` draws every numeric column against every other column. We first select only a few columns to keep the grid small.

```python {.marimo}
student_marks = student_df[
    ["attendance_rate", "study_hours", "gender", "Marks"]
]
student_marks
```

```python {.marimo}
sns.pairplot(data=student_marks)
```

The `kind` argument changes the type of the off-diagonal plots, for example to histograms (`"hist"`) or regression plots (`"reg"`).

```python {.marimo}
sns.pairplot(data=student_marks, kind="hist")
```

```python {.marimo}
sns.pairplot(data=student_marks, kind="reg")
```

With `hue` the points of each group get their own color.

```python {.marimo}
sns.pairplot(data=student_marks, hue="gender")
```

```python {.marimo}
sns.pairplot(data=student_marks, hue="gender", kind="reg")
```

## Joint Plot
`sns.jointplot()` shows the relation of two columns in the center and the distribution of each column on the sides.

```python {.marimo}
sns.jointplot(data=student_df, x="study_hours", y="Marks")
```

```python {.marimo}
sns.jointplot(data=student_df, x="study_hours", y="Marks", kind="kde")
```

```python {.marimo}
sns.jointplot(
    data=student_df, x="study_hours", y="Marks", kind="kde", hue="gender"
)
```