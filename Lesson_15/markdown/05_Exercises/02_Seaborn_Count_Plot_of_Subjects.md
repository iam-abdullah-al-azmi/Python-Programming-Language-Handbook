---
title: Seaborn and Plotly Visualization Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Here, you have to draw a Seaborn count plot of how many students are in each subject, split by gender.

```python {.marimo hide_code="true"}
import pandas as pd
import seaborn as sns
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent.parent / "sns_data.csv")

ax = sns.countplot(data=df, x="subject", hue="gender")
ax
```