---
title: Pandas Data Cleaning and Analysis
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Missing Values and Duplicates
Learn how to find missing values and unique values, and how to remove or fill missing data and remove duplicate rows.

```python {.marimo}
from pathlib import Path

import pandas as pd

folder = Path(__file__).resolve().parent
df = pd.read_csv(folder / "student_data.csv")
df.head()
```

## Finding missing values
Missing values are stored as NaN. `isnull` marks them with True, `notnull` is the opposite and `hasnans` tells whether a Series has any.

```python {.marimo}
print(df["Data Structure Marks"].isnull().head(8))
```

```python {.marimo}
print(df["Data Structure Marks"].notnull().head(8))
```

```python {.marimo}
print(df["Data Structure Marks"].hasnans)
print(df["StudentID"].hasnans)
```

```python {.marimo}
# isnull on the whole DataFrame, then count the True values per column
print(df.isnull().head())
print(df.isnull().sum())
```

## Unique values
`unique()` only works on a Series, not on a whole DataFrame. It includes NaN as a value, while `nunique()` ignores it.

```python {.marimo}
print(df["Instructor"].unique())
print(len(df["Instructor"].unique()))
```

```python {.marimo}
print(df["Algorithm Marks"].unique())
print(len(df["Algorithm Marks"].unique()))
```

```python {.marimo}
# without the null value
print(df["Algorithm Marks"].nunique())
print(df.nunique())
```

## Dropping missing values
`dropna` removes rows that contain a missing value. `how="all"` removes only rows where every value is missing, and `subset` limits the check to the chosen columns.

```python {.marimo}
print(len(df), "rows before,", len(df.dropna()), "after dropna()")
```

```python {.marimo}
# only rows that are missing every value are removed
print(len(df.dropna(how="all")))
```

```python {.marimo}
# removing rows with a null in the Python Marks column
print(len(df.dropna(subset=["Python Marks"])))
```

```python {.marimo}
# removing rows with a null in multiple columns
print(len(df.dropna(subset=["Python Marks", "Data Structure Marks"])))
```

## Filling missing values
`fillna` replaces missing values with a constant or with a calculated value such as the column mean.

```python {.marimo}
print(df.fillna(0).head(8))
```

```python {.marimo}
print(df["FullName"].fillna("unknown").head())
```

```python {.marimo}
print(df["Python Marks"].fillna(df["Python Marks"].mean().round(2)).head(8))
```

## Duplicates
`duplicated` marks every row that repeats an earlier row. This file (`New_Student_Info.csv`) was saved from the previous notebook, with the row index stored in the first column.

```python {.marimo}
students = pd.read_csv(folder / "New_Student_Info.csv", index_col=0)
students.head()
```

```python {.marimo}
print(students.duplicated().sum())
print(students.drop_duplicates().shape)
```

No complete row repeats here, so we add copies of two rows on purpose and try again.

```python {.marimo}
with_copies = pd.concat([students, students.iloc[[0, 1]]], ignore_index=True)
print(with_copies.shape)
print(with_copies.duplicated().sum())
print(with_copies.drop_duplicates().shape)
```

`drop_duplicates` returns a new DataFrame. Use `inplace=True` to change the original instead. The `subset` argument compares only some columns and `keep` chooses which copy survives (`"first"`, `"last"` or `False` to drop all copies).

```python {.marimo}
# keeps the first student of each completion status
print(students.drop_duplicates(subset=["CompletionStatus"])[["FullName", "CompletionStatus"]])
```

```python {.marimo}
print(students.drop_duplicates(subset=["Country"])[["FullName", "Country"]])
```

```python {.marimo}
# keep the last student of each completion status
print(students.drop_duplicates(subset=["CompletionStatus"], keep="last")[["FullName", "CompletionStatus"]])
```