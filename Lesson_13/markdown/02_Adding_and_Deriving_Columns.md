---
title: Pandas Data Cleaning and Analysis
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Adding and Deriving Columns
Learn how to create new columns from a constant, from arithmetic on other columns, from conditions with `np.where`, and by splitting text.

```python {.marimo}
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd

df = pd.read_csv(Path(__file__).resolve().parent / "student_data.csv")
df.head()
```

## Adding a column
Assigning to a new column name creates it. A single value is repeated for every row.

```python {.marimo}
df["Country"] = "Bangladesh"
print(df[["FullName", "Country"]].head())
```

## Column arithmetic
Arithmetic between columns is done element by element. A missing value (NaN) in any term makes the result NaN.

```python {.marimo}
df["Total Marks"] = df["Algorithm Marks"] + df["Python Marks"] + df["Data Structure Marks"]
print(df[["FullName", "Total Marks"]].head())
```

## Conditional columns with np.where
`np.where(condition, value_if_true, value_if_false)` builds a column from a condition.

```python {.marimo}
df["A+ in DS"] = np.where(df["Data Structure Marks"] > 90, "A+", "A")
print(df[["FullName", "Data Structure Marks", "A+ in DS"]].head())
```

```python {.marimo}
df["Passed in DS"] = np.where(df["Data Structure Marks"] > 70, "Passed", "Failed")
print(df[["FullName", "Data Structure Marks", "Passed in DS"]].head())
```

## Splitting text into columns
`str.split` splits every value; `.str[0]` then picks the first piece, `.str[1]` the second.

```python {.marimo}
df["First Name"] = df["FullName"].str.split(" ").str[0]
df["Last Name"] = df["FullName"].str.split(" ").str[1]
print(df[["FullName", "First Name", "Last Name"]].head())
```

```python {.marimo}
df
print(df.shape)
print(df.columns.tolist())
```

## Saving the result
`to_csv` writes the DataFrame to a file. To keep the repository clean the file is written to a temporary folder, read back, and deleted again.

```python {.marimo}
with tempfile.TemporaryDirectory() as _tmp:
    _filepath = Path(_tmp) / "New_Student_Info.csv"
    df.to_csv(_filepath)
    print(_filepath.name, "written with", len(_filepath.read_text().splitlines()), "lines")
    print(pd.read_csv(_filepath).columns.tolist())
```

Notice the extra first column named `Unnamed: 0` when the file is read back: it is the old row index that `to_csv` saved. Use `df.to_csv(path, index=False)` to leave it out, or read with `index_col=0` to restore it as the index.