---
title: Functional Tools and Generators Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Use map() with a lambda function to square every number in a list, then use filter() with a lambda function to keep only the squares greater than 20.

```python {.marimo hide_code="true"}
numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda value: value**2, numbers))
print(squares)

large_squares = list(filter(lambda value: value > 20, squares))
print(large_squares)
```