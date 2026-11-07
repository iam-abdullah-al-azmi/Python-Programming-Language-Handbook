---
title: Matplotlib Visualization Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Here, you have to plot Programming and Digital Marketing enrollment together, using different colors, markers and a legend.

```python {.marimo hide_code="true"}
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

df = pd.read_csv(Path(__file__).resolve().parent.parent / "enrollment_data.csv")

plt.title("Programming vs Digital Marketing Enrollment")
plt.xlabel("Year")
plt.ylabel("Enrollment")
plt.plot(
    df["Year"], df["Programming"], label="Programming", color="#32a852", marker="o"
)
plt.plot(
    df["Year"],
    df["Digital Marketing"],
    label="Digital Marketing",
    color="#8b32a8",
    linestyle="dotted",
    marker="o",
)
plt.legend()
plt.grid()
plt.gca()
```