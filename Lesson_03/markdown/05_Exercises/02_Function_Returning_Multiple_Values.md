---
title: Functions Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Write a function that takes a list of numbers and returns the minimum, maximum and sum together, then unpack the returned tuple.

```python {.marimo hide_code="true"}
def list_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = list_stats([4, 9, 1, 7, 3])
print(f"Min: {minimum} | Max: {maximum} | Sum: {total}")
```