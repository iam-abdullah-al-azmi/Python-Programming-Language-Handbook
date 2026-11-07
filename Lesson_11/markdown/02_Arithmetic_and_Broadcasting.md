---
title: NumPy Operations
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Arithmetic and Broadcasting
Learn how to add, subtract, multiply and divide arrays element by element, use NumPy's math functions, and combine arrays of different shapes with broadcasting.
<!---->
## Lists versus arrays
Adding two Python lists joins them. Adding two NumPy arrays adds the elements one by one.

```python {.marimo}
_list_one = [i for i in range(5)]
_list_two = [i for i in range(5, 10)]
print(_list_one + _list_two)
```

```python {.marimo}
import numpy as np
```

```python {.marimo}
array_one = np.linspace(1, 5, 5, dtype=np.int64)
array_two = np.linspace(6, 10, 5, dtype=np.int64)
print(f"{array_one}\n{array_two}")
print(f"summation: {array_one + array_two}, subtraction: {array_one - array_two}, multiplication: {array_one * array_two}, division: {np.round(array_one / array_two, 3)}")
```

The same operations are available as functions: `np.add`, `np.subtract`, `np.multiply` and `np.divide`.

```python {.marimo}
print(f"summation: {np.add(array_one, array_two)}, subtraction: {np.subtract(array_one, array_two)}, multiplication: {np.multiply(array_one, array_two)}, division: {np.round(np.divide(array_one, array_two), 3)}")
```

## Mathematical functions
NumPy has many functions that work on every element: `sin`, `cos`, `tan` (they take values in radians), `rad2deg`, `log10` and more. `np.round` limits the number of decimals.

```python {.marimo}
sin_vals = np.sin(array_one)  # sin, cos, tan takes values in radian unit
print(np.round(sin_vals, 3))
deg_con = np.rad2deg(array_one)
print(np.round(deg_con, 3))
base_ten_log_val = np.log10(array_one)
print(np.round(base_ten_log_val, 3))
```

## Broadcasting
Broadcasting lets NumPy combine arrays of different shapes: the smaller array is stretched across the bigger one.
A single number is stretched over the whole array, and a 1D array of 5 values is stretched over every row of a 2 x 5 array.

```python {.marimo}
print(array_one * 10)  # a single number is stretched to every element

array_one_2 = array_one ** 2
print(array_one_2)
array_three = np.linspace(5, 15, 10, dtype=np.int64)
array_three = array_three.reshape(2, 5)
print(array_three)
array_three = array_three ** 2
print(array_three)
array_four = array_one_2 + array_three  # shape (5,) + shape (2, 5) -> shape (2, 5)
print(array_four)
```