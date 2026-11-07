---
title: Python Basics Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Here, you have to take an input from the user and convert it to an integer.

```python {.marimo hide_code="true"}
val = input("Enter a number: ")
print(f"Value before conversion: {val} | Type: {type(val)}")
val = int(val)
print(f"Value after conversion: {val} | Type: {type(val)}")
```