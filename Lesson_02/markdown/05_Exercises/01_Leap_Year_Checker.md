---
title: Conditionals and Loops Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Check whether a year is a leap year. A year is a leap year if it is divisible by 4 but not by 100, or if it is divisible by 400.

```python {.marimo hide_code="true"}
year = 2100
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```