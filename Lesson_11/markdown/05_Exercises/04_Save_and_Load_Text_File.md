---
title: NumPy Operations Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Save a small 2D array to a temporary CSV text file with savetxt and read it back with genfromtxt.

```python {.marimo hide_code="true"}
import tempfile
from pathlib import Path

import numpy as np

_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

with tempfile.TemporaryDirectory() as _folder:
    _path = Path(_folder) / "numbers.txt"
    np.savetxt(_path, _data, delimiter=",", fmt="%d")
    _loaded = np.genfromtxt(_path, delimiter=",")

print("Loaded array:\n", _loaded)
print("Shape:", _loaded.shape)
```