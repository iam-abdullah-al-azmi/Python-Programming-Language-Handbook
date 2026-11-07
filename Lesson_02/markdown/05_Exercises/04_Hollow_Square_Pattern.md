---
title: Conditionals and Loops Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Print a hollow square pattern of size 5 using the + symbol.

```python {.marimo hide_code="true"}
n = 5
for i in range(1, n + 1):
    for k in range(1, n + 1):
        if i == 1 or i == n or k == 1 or k == n:
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()
```