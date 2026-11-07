---
title: Pandas Data Cleaning and Analysis
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Filtering Rows with Conditions and Text
Learn how to keep only the rows you want, using boolean conditions on numbers and the `str.contains` method (with regular expressions) on text.

```python {.marimo}
from pathlib import Path

import pandas as pd

students = pd.read_csv(Path(__file__).resolve().parent / "student_data.csv")
```

## Filtering with conditions
A comparison such as `df["Python Marks"] > 85` produces a boolean Series (True or False for every row). Passing it to `loc` keeps only the rows that are True.

```python {.marimo}
print((students["Python Marks"] > 85).head())
print(students.loc[students["Python Marks"] > 85, ["FullName", "Python Marks"]])
```

Combine conditions with `&` (and), `|` (or) and `~` (not). Every condition must be wrapped in parentheses.

```python {.marimo}
print(students.loc[(students["Python Marks"] > 85) & (students["Instructor"] == "Mr. Karim"), ["FullName", "Instructor", "Python Marks"]])
print(students.loc[(students["Location"] == "Dhaka") | (students["Location"] == "Sylhet"), ["FullName", "Location"]])
```

```python {.marimo}
# isin checks membership in a list, between checks a range (both ends included)
print(students.loc[students["Location"].isin(["Sylhet", "Khulna"]), ["FullName", "Location"]])
print(students.loc[students["Python Marks"].between(80, 85), ["FullName", "Python Marks"]])
```

## Filtering text with str.contains
The `.str` accessor applies string methods to every value of a text column. We use a small DataFrame to practise.

```python {.marimo}
_data = {
    "Name": ["Alice one", "Bob two", "Cha one", "Dada two", "Esa One"],
    "City": ["Los abcd RK", "New efgh RK", "Los ijkl RKA", "new mnop RKA", "qrst new los rka"],
    "Department": ["EEE", "MPE", "EEE", "CSE", "SWE"],
    "Salary": [10, 20, 30, 40, 50],
}

df = pd.DataFrame(_data)
df
print(df)
```

```python {.marimo}
# case sensitive: "One" in "Esa One" does not match
print(df.loc[df["Name"].str.contains("one")])
```

```python {.marimo}
# case=False ignores upper/lower case
print(df.loc[df["Name"].str.contains("one", case=False)])
```

```python {.marimo}
print(df.loc[df["City"].str.contains(r"Los", case=False)])
```

`str.contains` accepts regular expressions: `^` means "starts with", `$` means "ends with", `[...]` matches any one of the listed characters and `|` means "or".

```python {.marimo}
# starts with Los
print(df.loc[df["City"].str.contains(r"^Los", case=False)])
```

```python {.marimo}
print(df.loc[df["City"].str.contains(r"RK", case=False)])
```

```python {.marimo}
# ends with RK
print(df.loc[df["City"].str.contains(r"RK$", case=False)])
```

```python {.marimo}
# names that start with a vowel
print(df.loc[df["Name"].str.contains(r"^[AEIOU]", case=False)])
```

```python {.marimo}
# city contains RK or RKA
print(df.loc[df["City"].str.contains(r"RK|RKA", case=False)])
```

For simple prefixes and suffixes, `str.startswith` and `str.endswith` do the same job without regular expressions.

```python {.marimo}
print(df.loc[df["City"].str.startswith("Los")])
print(df.loc[df["Name"].str.endswith("two")])
```