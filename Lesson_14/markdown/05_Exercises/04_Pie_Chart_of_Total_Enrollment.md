---
title: Matplotlib Visualization Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Here, you have to draw a pie chart showing the share of total enrollment between Programming and Digital Marketing over all years.

```python {.marimo hide_code="true"}
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

df = pd.read_csv(Path(__file__).resolve().parent.parent / "enrollment_data.csv")

totals = [df["Programming"].sum(), df["Digital Marketing"].sum()]

plt.pie(totals, labels=["Programming", "Digital Marketing"], autopct="%1.1f%%")
plt.title("Share of Total Enrollment")
plt.gca()
```