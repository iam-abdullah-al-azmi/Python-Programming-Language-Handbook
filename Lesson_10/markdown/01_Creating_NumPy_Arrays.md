---
title: NumPy Foundations
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Creating NumPy Arrays
Learn why NumPy arrays are better than Python lists for numbers, and how to create 1D, 2D and 3D arrays from lists, tuples, sets and dictionaries.
<!---->
## Why NumPy
A list is not homogeneous: it can contain mixed data types, which becomes a problem when handling large datasets and applying operations on them.
NumPy's `ndarray` solves this: every element has the same type and an operation is applied to all the elements at once (SIMD = Single Instruction Multiple Data).

Suppose we want to multiply every value by an integer. For a list, `*` repeats the list, so we need a list comprehension to get the multiplication.

```python {.marimo}
_lst = [1, 2, 3]
print(_lst * 5)
_lst = [x * 5 for x in _lst]
print(_lst)
# _lst = [i for i in range(10000000)]  # a very large list makes the computer slow
```

```python {.marimo}
import numpy as np
```

## Arrays of different dimensions
`np.array()` turns a list into an array. A list of lists becomes a 2D array and a list of lists of lists becomes a 3D array.
With an array, `*` multiplies every element.

```python {.marimo}
array_one = np.array([i for i in range(5)])
print(array_one * 5, type(array_one), array_one.ndim)

array_two = np.array([[i for i in range(5)], [i for i in range(5)]])
print(array_two)
print(array_two.ndim)

array_three = np.array([[[i for i in range(5)], [i for i in range(5)]], [[i for i in range(5)], [i for i in range(5)]]])
print(array_three)
print(array_three.ndim)
```

## Creating arrays from other Python types
- a tuple works like a list
- a set has no order and no indexes, so `np.array(set)` makes a single object, convert it to a list first
- a dictionary cannot be converted directly either; convert its keys, values or items instead

```python {.marimo}
# tuple
array_nine = np.array(tuple(i for i in range(5)))
print(array_nine, array_nine.dtype)

# set
array_ten = np.array(set(i for i in range(5)))
print(array_ten, array_ten.dtype)

array_ten = np.array(list(set(i for i in range(5))))
print(array_ten, array_ten.dtype)
```

```python {.marimo}
# dictionary
_dict = {chr(key + 64): val for key, val in zip(range(1, 6), range(5))}
_array_dict = np.array(_dict)
print(_array_dict, _array_dict.dtype, type(_dict.keys()), type(_dict.values()), type(_dict.items()))

_keys = np.array(list(_dict.keys()))
_values = np.array(list(_dict.values()))
_items = np.array(list(_dict.items()))

print(_keys, _values)
print(_items)
print(_keys.dtype, _values.dtype, _items.dtype)
```