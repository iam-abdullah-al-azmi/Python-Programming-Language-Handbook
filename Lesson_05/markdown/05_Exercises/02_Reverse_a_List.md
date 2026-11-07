---
title: Strings and Lists Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Reverse the order of the elements in a list without using the reverse() method.

```python {.marimo hide_code="true"}
numbers = [4, 2, 9, 1, 5, 6]
reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])
print(f"Original list: {numbers}")
print(f"Reversed list: {reversed_numbers}")
```