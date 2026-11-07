---
title: Seaborn and Plotly Visualization Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Here, you have to draw a Plotly scatter plot of study_hours against test_score, colored by gender, sized by Tshirt_size, and showing subject and hostel on hover.

```python {.marimo hide_code="true"}
import pandas as pd
from pathlib import Path
import plotly.express as px

df = pd.read_csv(Path(__file__).resolve().parent.parent / "sns_data.csv")

fig = px.scatter(
    data_frame=df,
    x="study_hours",
    y="test_score",
    color="gender",
    size="Tshirt_size",
    hover_data=["subject", "hostel"],
)
fig
```