---
title: Python Basics Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Convert a given number to binary, octal, and hexadecimal using the format function. Then show the square root of the number rounded up with the math module, and the result of a bitwise AND with 15.

```python {.marimo hide_code="true"}
import math

num = 255
print(
    f"Decimal: {num} | Binary: {format(num, 'b')} | Octal: {format(num, 'o')} | Hexadecimal: {format(num, 'X')}"
)
print(f"Square root rounded up: {math.ceil(math.sqrt(num))}")
print(f"{num} & 15 = {num & 15} (binary {format(num & 15, 'b')})")
```