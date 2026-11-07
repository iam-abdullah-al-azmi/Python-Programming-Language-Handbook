---
title: Pandas Foundations
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Series and DataFrame Basics
Learn the two core pandas data structures: the Series (a single labelled column of data) and the DataFrame (a table made of several Series).

```python {.marimo}
from pathlib import Path

import pandas as pd
```

## Series
A Series is a one-dimensional labelled array. By default the labels (the index) are 0, 1, 2, ...

```python {.marimo}
marks = pd.Series([88, 92, 75], name="Python Marks")
print(marks)
print(type(marks))
```

```python {.marimo}
# a Series has values, an index and a dtype
print(marks.values)
print(marks.index)
print(marks.dtype)
```

You can choose your own index labels, or build a Series from a dictionary (keys become the labels).

```python {.marimo}
named = pd.Series([88, 92, 75], index=["Alif", "Fatima", "Imran"], name="Python Marks")
print(named)
print(named["Fatima"])
print(named.mean())
```

```python {.marimo}
from_dict = pd.Series({"Alif": 88, "Fatima": 92, "Imran": 75})
print(from_dict)
```

## DataFrame
A DataFrame is tabular data. The simplest way to create one is from a dictionary where every key is a column name and every value is a list of the column's data.

```python {.marimo}
students = pd.DataFrame(
    {
        "Name": ["Alif", "Fatima", "Imran"],
        "Python Marks": [88, 92, 75],
        "City": ["Dhaka", "Chattogram", "Sylhet"],
    }
)
print(type(students))
print(students)
```

```python {.marimo}
# shape is (number of rows, number of columns)
print(students.shape)
print(students.columns)
print(students.dtypes)
```

A DataFrame can also be built from a list of dictionaries, one dictionary per row.

```python {.marimo}
rows = pd.DataFrame(
    [
        {"Name": "Alif", "Python Marks": 88},
        {"Name": "Fatima", "Python Marks": 92},
    ]
)
print(rows)
```

## DataFrame versus Series
DataFrame is tabular data and Series is a single row or a single column of it. Selecting one column with square brackets gives a Series.

```python {.marimo}
print(type(students["Python Marks"]))
print(students["Python Marks"])
```

The same is true for a DataFrame loaded from a file.

```python {.marimo}
df = pd.read_csv(Path(__file__).resolve().parent / "student_data.csv")
print(type(df))
print(type(df["StudentID"]))
df.head()
```