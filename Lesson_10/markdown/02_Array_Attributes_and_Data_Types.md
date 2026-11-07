---
title: NumPy Foundations
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Array Attributes and Data Types
Learn how to inspect an array with `ndim`, `shape`, `size` and `dtype`, how NumPy upcasts mixed values, and how to choose or change a data type.

```python {.marimo}
import numpy as np
```

```python {.marimo}
array_one = np.array([i for i in range(5)])
array_two = np.array([[i for i in range(5)], [i for i in range(5)]])
array_three = np.array([[[i for i in range(5)], [i for i in range(5)]], [[i for i in range(5)], [i for i in range(5)]]])
```

## Attributes of an array
- `ndim`: number of dimensions
- `shape`: the length of every dimension
- `dtype`: the data type of the elements
- `size`: the total number of elements

```python {.marimo}
# dimension
print(array_one.ndim, array_two.ndim, array_three.ndim)

# shape
print(array_one.shape, array_two.shape, array_three.shape)

# data type
print(array_one.dtype, array_two.dtype, array_three.dtype)

# size
print(array_one.size, array_two.size, array_three.size)
```

## Upcasting
All elements of an array share one data type. When values of different types are mixed, NumPy upcasts everything to the type that can hold all of them:
integers and floats become float, and anything mixed with text becomes a string (`U` is the string data type in NumPy).

```python {.marimo}
array_four = np.array([i for i in range(5)])
array_five = np.array([float(i) for i in range(5)])
array_six = np.array([i if i % 2 == 0 else float(i) for i in range(5)])
array_seven = np.array([i if i % 2 == 0 else (chr(64 + i) if i == 1 else float(i)) for i in range(5)])

print(array_four, array_five, array_six, array_seven)
print(array_four.dtype, array_five.dtype, array_six.dtype, array_seven.dtype)
```

## Selecting a data type
Pass `dtype=` when creating the array, or change it later with `astype()`, which returns a new array.
A smaller type such as `int8` saves memory but only holds values from -128 to 127.

```python {.marimo}
array_eight = np.array([i for i in range(5)], dtype=np.int16)
print(array_eight.dtype)
array_eight = array_eight.astype(np.int8)
print(array_eight.dtype)

# The problem of int8 is that we can't use big numbers with it: a value greater than 127 shows an OverflowError
# array_eight = np.array([i for i in range(129)], dtype=np.int8)
# print(array_eight, array_eight.dtype)
```