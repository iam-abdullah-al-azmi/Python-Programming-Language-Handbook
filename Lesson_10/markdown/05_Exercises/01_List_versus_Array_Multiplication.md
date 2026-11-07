---
title: NumPy Foundations Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Multiply a Python list and a NumPy array by 3 and explain the difference in the output.

```python {.marimo hide_code="true"}
import numpy as np

_lst = [1, 2, 3]
_arr = np.array(_lst)

print(f"List * 3  : {_lst * 3}  (the list is repeated)")
print(f"Array * 3 : {_arr * 3}  (every element is multiplied)")
```