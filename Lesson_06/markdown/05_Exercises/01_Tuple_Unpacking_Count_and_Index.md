---
title: Tuples, Sets and Dictionaries Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Swap the values of a, b and c by rotating them with tuple unpacking, then count how many times a value appears in a tuple and find the index of its first occurrence.

```python {.marimo hide_code="true"}
a, b, c = (5, 10, 15)
a, b, c = (c, a, b)
print(a, b, c)
```

```python {.marimo hide_code="true"}
tup = (10, 20, 10, 30, 10, 40)
print(f"Tuple: {tup}")
print(f"Count of 10: {tup.count(10)}")
print(f"First index of 30: {tup.index(30)}")
```