---
title: NumPy Foundations Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Create a 3x4 array with arange, change one element, then print the first row, the last column and the 2x2 block in the top-left corner.

```python {.marimo hide_code="true"}
import numpy as np

_arr = np.arange(1, 13).reshape(3, 4)
print("Original:\n", _arr)

_arr[1][2] = 100
print("After changing row 1, column 2 to 100:\n", _arr)

print("First row   :", _arr[0])
print("Last column :", _arr[:, -1])
print("Top-left 2x2:\n", _arr[0:2, 0:2])
```