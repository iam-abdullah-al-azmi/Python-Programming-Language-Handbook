---
title: Matplotlib Visualization Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Here, you have to draw a scatter plot of Chilling_Hours against IQ_Score using the x marker.

```python {.marimo hide_code="true"}
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_IQdata.csv")

plt.title("Relation between Chilling Hours and IQ Score")
plt.xlabel("Chilling Hours")
plt.ylabel("IQ Score")
plt.scatter(df["Chilling_Hours"], df["IQ_Score"], marker="x")
plt.grid()
plt.gca()
```