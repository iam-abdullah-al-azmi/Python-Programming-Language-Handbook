---
title: Pandas Data Cleaning and Analysis Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Keep the students with Python Marks above 85, then create a small DataFrame of names and cities and use str.contains to filter names containing one (any case), cities starting with Los, cities ending with RK and names starting with a vowel.

```python {.marimo hide_code="true"}
from pathlib import Path
import pandas as pd

students = pd.read_csv(Path(__file__).resolve().parent.parent / "student_data.csv")
print(students.loc[students["Python Marks"] > 85, ["FullName", "Python Marks"]])

df = pd.DataFrame(
    {
        "Name": ["Alice one", "Bob two", "Cha one", "Dada two", "Esa One"],
        "City": [
            "Los abcd RK",
            "New efgh RK",
            "Los ijkl RKA",
            "new mnop RKA",
            "qrst new los rka",
        ],
    }
)

print("Name contains 'one':\n", df.loc[df["Name"].str.contains("one", case=False)])
print(
    "City starts with Los:\n", df.loc[df["City"].str.contains(r"^Los", case=False)]
)
print("City ends with RK:\n", df.loc[df["City"].str.contains(r"RK$", case=False)])
print(
    "Name starts with a vowel:\n",
    df.loc[df["Name"].str.contains(r"^[AEIOU]", case=False)],
)
```