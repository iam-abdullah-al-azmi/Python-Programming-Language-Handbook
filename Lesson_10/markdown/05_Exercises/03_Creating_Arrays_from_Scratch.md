---
title: NumPy Foundations Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Create arrays using zeros, ones, full and random.randint (seed the generator), then an array of even numbers from 2 to 18 with arange, 5 evenly spaced values between 2 and 20 with linspace and a 4x4 identity matrix. Print their shapes and values.

```python {.marimo hide_code="true"}
import numpy as np

np.random.seed(42)
print("zeros (2, 3):\n", np.zeros((2, 3)))
print("ones (2, 3):\n", np.ones((2, 3)))
print("full (3, 4) with 10:\n", np.full((3, 4), 10))

_rand = np.random.randint(1, 10, (3, 4))
print("random ints (3, 4):\n", _rand)
print("shape:", _rand.shape)

_even = np.arange(2, 20, 2)
print("arange  :", _even, "| size:", _even.size)
print("linspace:", np.linspace(2, 20, 5))
print("identity 4x4:\n", np.eye(4, dtype=np.int64))
```