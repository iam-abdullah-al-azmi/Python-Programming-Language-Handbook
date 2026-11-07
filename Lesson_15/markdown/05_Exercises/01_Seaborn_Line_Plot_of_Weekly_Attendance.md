---
title: Seaborn and Plotly Visualization Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Here, you have to draw a Seaborn line plot of attendance_rate by week, with a separate line for each gender and no error band.

```python {.marimo hide_code="true"}
import pandas as pd
import seaborn as sns
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent.parent / "sns_data.csv")

ax = sns.lineplot(
    data=df, x="week", y="attendance_rate", hue="gender", errorbar=None
)
ax
```