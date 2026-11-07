---
title: Functional Tools and Generators Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Use reduce() with a lambda function to find the product of all numbers in a list, and the largest number in the same list.

```python {.marimo hide_code="true"}
from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")

largest = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Largest: {largest}")
```