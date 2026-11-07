---
title: NumPy Foundations
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Indexing and Slicing Arrays
Learn how to read and change single elements of an array with indexes and how to take parts of an array with slices.

```python {.marimo}
import numpy as np
```

## Indexing
An index picks one element, starting from 0. In a 2D array the first index selects the row and the second the column. Assigning to an index changes the element.

```python {.marimo}
array_one = np.arange(5)
array_two = np.array([np.arange(5), np.arange(5)])
print(array_one.shape, array_two.shape)

array_one[2] = 10
print(array_one)

array_two[0][2] = 84
print(array_two)
```

## Slicing
A slice `start:stop:step` takes a range of elements (the stop index is not included). For a 2D array give one slice for the rows and one for the columns, separated by a comma.

```python {.marimo}
array_one_1 = array_one[1:4]
print(array_one_1)

array_two_1 = array_two[0:1:1, 0::1]
print(array_two_1)
```

## More ways to select elements
- negative indexes count from the end (`-1` is the last element)
- `arr[row, column]` is a shorter way to write `arr[row][column]`
- a single `:` selects the whole dimension
- a condition such as `arr > 5` creates a boolean mask that selects only the matching elements

```python {.marimo}
_matrix = np.arange(1, 13).reshape(3, 4)
print(_matrix)

print(_matrix[-1])  # last row
print(_matrix[1, 2])  # same as _matrix[1][2]
print(_matrix[:, 0])  # first column
print(_matrix[0:2, 1:3])  # rows 0-1 and columns 1-2
print(_matrix[_matrix > 8])  # boolean mask
```

## A slice is a view, not a copy
A slice shares its memory with the original array, so changing the slice changes the original. Use `copy()` when you need an independent array.

```python {.marimo}
_original = np.arange(5)
_view = _original[1:4]
_view[0] = 99
print(_original)

_copy = _original[1:4].copy()
_copy[0] = -1
print(_original, _copy)
```