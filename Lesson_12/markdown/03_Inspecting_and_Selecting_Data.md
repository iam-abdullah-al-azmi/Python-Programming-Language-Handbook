---
title: Pandas Foundations
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Inspecting and Selecting Data
Learn how to look at a DataFrame (head, tail, info, describe) and how to select columns and rows with square brackets, `loc` and `iloc`.

```python {.marimo}
from pathlib import Path

import numpy as np
import pandas as pd

df = pd.read_csv(Path(__file__).resolve().parent / "student_data.csv")
```

## Inspecting a DataFrame

```python {.marimo}
print(df.head())
```

```python {.marimo}
print(df.tail(3))
```

```python {.marimo}
# the column names, as an Index, a list and a NumPy array
print(df.columns)

columns_list = list(df.columns)
print(columns_list)

columns_array = np.array(columns_list)
print(columns_array, columns_array.dtype)
```

```python {.marimo}
print(df.index)
print(df.shape)
print(df.dtypes)
```

```python {.marimo}
# column names, non-null counts and data types
df.info()
```

```python {.marimo}
# random rows; random_state makes the sample repeatable
print(df.sample(5, random_state=1))
```

```python {.marimo}
# count, mean, std, min, quartiles and max of the numeric columns
print(df.describe())
```

## Selecting columns
Square brackets with a column name give a Series. A list of names gives a DataFrame.

```python {.marimo}
print(type(df["FullName"]))
print(df["FullName"].head())
```

```python {.marimo}
print(type(df[["FullName", "Python Marks"]]))
print(df[["FullName", "Python Marks"]].head())
```

## Selecting rows and columns with loc
`loc` selects by label: `df.loc[row_start:row_end, col_start:col_end]`. Unlike normal Python slicing, the end label of a `loc` slice is included.

```python {.marimo}
# a single row gives a Series
print(df.loc[0])
print(type(df.loc[0]))
```

```python {.marimo}
# multiple rows
print(df.loc[[2, 3, 19]])
```

```python {.marimo}
# multiple rows using a range (3 to 7 inclusive)
print(df.loc[3:7])
```

```python {.marimo}
# single column
print(df.loc[:, ["Python Marks"]].head())
```

```python {.marimo}
# multiple columns
print(df.loc[:, ["Python Marks", "Algorithm Marks"]].head())
```

```python {.marimo}
# rows with columns
print(df.loc[3:7, ["CompletionStatus"]])
```

## Setting an index and selecting with iloc
`set_index` turns a column into the row labels. `iloc` always selects by integer position (the end of the slice is excluded, as in normal Python), while `loc` uses the labels.

```python {.marimo}
indexed = df.set_index("StudentID")
print(indexed.head(3))
```

```python {.marimo}
# position 3 up to (but not including) position 7
print(indexed.iloc[3:7])
```

```python {.marimo}
print(indexed.loc["PH1003"])
print(indexed.loc["PH1003", "FullName"])
```

```python {.marimo}
# loc uses labels, so slicing with numbers on a text index is an error
try:
    indexed.loc[3:7]
except TypeError as _error:
    print("TypeError:", _error)
```