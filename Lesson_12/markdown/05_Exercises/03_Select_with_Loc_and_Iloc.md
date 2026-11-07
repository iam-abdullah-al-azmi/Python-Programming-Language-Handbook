---
title: Pandas Foundations Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Select the FullName column (check that it is a Series) and print describe() for the marks columns. Using loc, select row 0, rows 3 to 7 and the CompletionStatus of rows 3 to 7. Then set StudentID as the index, select the rows at positions 3 to 6 with iloc and the row labelled PH1003 with loc.

```python {.marimo hide_code="true"}
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
_names = df["FullName"]
print(type(_names))
print(_names.head())

_marks = ["Data Structure Marks", "Algorithm Marks", "Python Marks"]
print(df[_marks].describe())

print("Row 0:\n", df.loc[0])
print("Rows 3 to 7:\n", df.loc[3:7])
print("CompletionStatus rows 3-7:\n", df.loc[3:7, ["CompletionStatus"]])

_indexed = df.set_index("StudentID")
print("iloc[3:7]:\n", _indexed.iloc[3:7])
print("loc PH1003:\n", _indexed.loc["PH1003"])
```