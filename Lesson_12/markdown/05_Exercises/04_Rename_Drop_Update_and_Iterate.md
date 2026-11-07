---
title: Pandas Foundations Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: On a copy of the DataFrame rename FullName to Full Name, drop the Instructor column and drop row 0. Then set the Python Marks of row 1 to 90, add 2 marks to the Python Marks of rows 1 to 3, and loop over the first five rows with iterrows and itertuples printing each student's name and Python Marks.

```python {.marimo hide_code="true"}
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
_copy = df.copy()
_copy = _copy.rename(columns={"FullName": "Full Name"})
_copy = _copy.drop("Instructor", axis=1)
_copy = _copy.drop(0)
print(_copy.columns.tolist())
print("Rows before:", len(df), "| after:", len(_copy))

_copy = df.copy()
print("Before:\n", _copy.loc[1:3, ["FullName", "Python Marks"]])
_copy.loc[1, "Python Marks"] = 90
_copy.loc[1:3, "Python Marks"] += 2
print("After:\n", _copy.loc[1:3, ["FullName", "Python Marks"]])

_first = _copy.head(5)
print("Using iterrows:")
for _i, _row in _first.iterrows():
    print(f"{_i}: {_row['FullName']} -> {_row['Python Marks']}")
print("Using itertuples:")
for _row in _first.itertuples():
    print(f"{_row.Index}: {_row.FullName} -> {_row[5]}")
```