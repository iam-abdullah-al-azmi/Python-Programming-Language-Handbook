---
title: Strings and Lists Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Create a list of the squares of all even numbers from 1 to 20 using list comprehension.

```python {.marimo hide_code="true"}
squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(f"Squares of even numbers: {squares}")
```