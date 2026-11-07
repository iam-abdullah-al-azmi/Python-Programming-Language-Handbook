---
title: Conditionals and Loops Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Reverse the digits of a given number using a while loop.

```python {.marimo hide_code="true"}
temp_num = 12345  # temp_num = eval(input("Enter a number: "))
sum_of_reversed = 0
while temp_num > 0:
    rem = temp_num % 10
    sum_of_reversed = sum_of_reversed * 10 + rem
    temp_num = temp_num // 10
print(sum_of_reversed)
```