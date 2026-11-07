---
title: Exceptions, Files and Modules Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Write a function that divides two values and handles ZeroDivisionError and TypeError separately. Test it with valid and invalid inputs.

```python {.marimo hide_code="true"}
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both values must be numbers"
    else:
        return result

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "two"))
```