---
title: Pandas Data Cleaning and Analysis Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Add a Country column, a Total Marks column, a Passed in DS column (above 70) using np.where, and First Name and Last Name columns using str.split.

```python {.marimo hide_code="true"}
import numpy as np
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
df["Country"] = "Bangladesh"
df["Total Marks"] = (
    df["Data Structure Marks"] + df["Algorithm Marks"] + df["Python Marks"]
)
df["Passed in DS"] = np.where(df["Data Structure Marks"] > 70, "Passed", "Failed")
df["First Name"] = df["FullName"].str.split(" ").str[0]
df["Last Name"] = df["FullName"].str.split(" ").str[1]

print(
    df[
        [
            "FullName",
            "First Name",
            "Last Name",
            "Total Marks",
            "Passed in DS",
            "Country",
        ]
    ].head(10)
)
```