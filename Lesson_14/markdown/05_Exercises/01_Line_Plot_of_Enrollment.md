---
title: Matplotlib Visualization Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Here, you have to draw a line plot of Programming enrollment against Year, with a title, axis labels and a grid.

```python {.marimo hide_code="true"}
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

df = pd.read_csv(Path(__file__).resolve().parent.parent / "enrollment_data.csv")

plt.title("Programming Enrollment by Year")
plt.xlabel("Year")
plt.ylabel("Enrollment")
plt.plot(df["Year"], df["Programming"])
plt.grid()
plt.gca()
```