---
title: Tuples, Sets and Dictionaries Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Find the common elements of two lists using the set intersection() method, then remove the duplicate values from a list using a set and print the sorted unique values.

```python {.marimo hide_code="true"}
list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]
common = set(list_a).intersection(set(list_b))
print(f"Common elements: {sorted(common)}")
```

```python {.marimo hide_code="true"}
numbers = [3, 1, 2, 3, 4, 1, 5, 2, 5]
unique = set(numbers)
print(f"Original list: {numbers}")
print(f"Unique values: {sorted(unique)}")
```