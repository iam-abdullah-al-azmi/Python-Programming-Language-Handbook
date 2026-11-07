---
title: Pandas Foundations
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Reading and Writing Data Files
Learn how to load data from CSV, JSON, Excel and Parquet files into a DataFrame, and how to write a DataFrame back out to those formats.

```python {.marimo}
import tempfile
from pathlib import Path

import pandas as pd

folder = Path(__file__).resolve().parent
```

## Reading files
Each file format has its own `read_*` function. They all return a DataFrame. Start with a CSV (comma separated values) file.

```python {.marimo}
df = pd.read_csv(folder / "student_data.csv")
df.head()
```

`read_csv` has many optional arguments: `usecols` picks columns, `nrows` reads only the first rows and `index_col` chooses the column used as the index.

```python {.marimo}
print(pd.read_csv(folder / "student_data.csv", usecols=["StudentID", "FullName"], nrows=3))
print(pd.read_csv(folder / "student_data.csv", index_col="StudentID").head(3))
```

JSON, Excel and Parquet files are read in the same way.

```python {.marimo}
json_df = pd.read_json(folder / "data.json")
json_df
```

```python {.marimo}
excel_df = pd.read_excel(folder / "phitron_student_marks.xlsx")
excel_df.head()
```

```python {.marimo}
parquet_df = pd.read_parquet(folder / "students.parquet")
parquet_df.head()
```

```python {.marimo}
for _name, _frame in [("csv", df), ("json", json_df), ("excel", excel_df), ("parquet", parquet_df)]:
    print(_name, _frame.shape)
```

## Writing files
`to_csv`, `to_json`, `to_excel` and `to_parquet` save a DataFrame. Here the files are written to a temporary folder that is deleted automatically, so nothing is left behind. Pass `index=False` to avoid saving the row index as an extra column.

```python {.marimo}
_small = df[["StudentID", "FullName", "Python Marks"]].head(3)

with tempfile.TemporaryDirectory() as _tmp:
    _out = Path(_tmp)

    _small.to_csv(_out / "small.csv", index=False)
    _small.to_json(_out / "small.json", orient="records", indent=2)
    _small.to_excel(_out / "small.xlsx", index=False)
    _small.to_parquet(_out / "small.parquet")

    print(sorted(_p.name for _p in _out.iterdir()))
    print((_out / "small.csv").read_text())
    print((_out / "small.json").read_text())

    print(pd.read_csv(_out / "small.csv"))
    print(pd.read_parquet(_out / "small.parquet"))
```