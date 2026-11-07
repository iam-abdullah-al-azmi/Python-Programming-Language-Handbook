---
title: Conditionals and Loops Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Find the sum of all even numbers from 1 to a given number using a for loop and an if statement.

```python {.marimo hide_code="true"}
ev_num = 10  # ev_num = int(input("Enter a number:"))
ev_sum = 0
for _i in range(1, ev_num + 1):
    if _i % 2 == 0:
        ev_sum += _i
print(f"Even sum is {ev_sum}")
```