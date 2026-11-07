---
title: NumPy Operations Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Add, subtract, multiply and divide two arrays element-wise, then square a 2x5 array and add a 1D array to it using broadcasting.

```python {.marimo hide_code="true"}
import numpy as np

_a = np.array([1, 2, 3, 4, 5])
_b = np.array([6, 7, 8, 9, 10])
print("add     :", _a + _b)
print("subtract:", _a - _b)
print("multiply:", _a * _b)
print("divide  :", np.round(_a / _b, 3))

_matrix = np.arange(1, 11).reshape(2, 5) ** 2
print("Squared 2x5:\n", _matrix)
print("Broadcast add:\n", _matrix + _a)
```