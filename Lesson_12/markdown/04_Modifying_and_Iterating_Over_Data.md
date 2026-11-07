---
title: Pandas Foundations
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Modifying and Iterating Over Data
Learn how to rename and drop columns and rows, update values with `loc`, and loop over the rows of a DataFrame.

```python {.marimo}
from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).resolve().parent / "student_data.csv")
```

## Renaming columns
Most DataFrame methods return a new DataFrame and leave the original untouched. Passing `inplace=True` modifies the original object instead of making a copy (and returns `None`).

```python {.marimo}
renamed = df.rename(
    columns={
        "FullName": "Full Name",
        "CompletionStatus": "Completion Status",
        "EnrollmentDate": "Enrollment Date",
    }
)
print(renamed.columns.tolist())
print(df.columns.tolist())
```

## Dropping rows and columns
`drop` removes rows by default; pass `axis=1` (or `columns=`) to remove columns.

```python {.marimo}
# row deletion
print(df.drop(0).head(3))
```

```python {.marimo}
# column deletion
print(df.drop("Instructor", axis=1).columns.tolist())
```

```python {.marimo}
# the original DataFrame is unchanged
print(df.shape)
```

## Updating values
`loc` can also assign: `df.loc[row, column] = value`. Compound operators such as `+=` work on a whole slice.

```python {.marimo}
df.loc[1, "Python Marks"] = 90
df.loc[1, "CompletionStatus"] = "Completed"
print(df.loc[0:3, ["FullName", "Python Marks", "CompletionStatus"]])
```

```python {.marimo}
df.loc[1:3, "Python Marks"] += 2
print(df.loc[0:3, ["FullName", "Python Marks"]])
```

## Iterating over rows
`iterrows` yields an (index, Series) pair for each row. `itertuples` yields a named tuple per row and is faster.

```python {.marimo}
for _i, _row in df.head(3).iterrows():
    print(f"{_i}: {_row['FullName']} -> {_row['Python Marks']}")
```

```python {.marimo}
for _row in df.head(3).itertuples():
    print(_row)
```

```python {.marimo}
for _row in df.head(3).itertuples():
    print(_row.Index, _row.FullName, _row.Location)
```