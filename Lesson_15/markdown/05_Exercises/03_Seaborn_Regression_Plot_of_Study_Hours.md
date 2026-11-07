---
title: Seaborn and Plotly Visualization Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Here, you have to draw a Seaborn regression plot of study_hours against test_score.

```python {.marimo hide_code="true"}
import pandas as pd
import seaborn as sns
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent.parent / "sns_data.csv")

ax = sns.regplot(data=df, x="study_hours", y="test_score")
ax
```