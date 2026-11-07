---
title: NumPy Foundations
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Creating Special Arrays
Learn how to build arrays from scratch: filled with zeros, ones or a chosen value, random numbers, number ranges, and identity or diagonal matrices.

```python {.marimo}
import numpy as np
```

## Zeros, ones and the like functions
`np.zeros` and `np.ones` take the shape as a tuple. `np.zeros_like` and `np.ones_like` copy the shape of an existing array.

```python {.marimo}
array_template = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

array_twelve = np.zeros((2, 3))
print(array_twelve, array_twelve.dtype)

array_thirteen = np.zeros_like(array_template)
print(array_thirteen, array_thirteen.dtype, array_thirteen.shape, array_template.shape)

array_fourteen = np.ones((2, 3))
array_fifteen = np.ones_like(array_thirteen)
print(array_fourteen.shape, array_fifteen.shape)
```

## Empty and full arrays
`np.empty` only reserves the memory, so the values you see are whatever was there before and can be anything.
`np.full` fills the array with a chosen value.

```python {.marimo}
array_sixteen = np.empty((3, 4))
print(array_sixteen)

array_seventeen = np.full((3, 4), 10)
print(array_seventeen)

array_seventeen = np.full((3, 4), True)
print(array_seventeen)

array_seventeen = np.full((3, 4), np.inf)
print(array_seventeen)
```

## Random arrays
`np.random.seed()` makes the random numbers repeatable. `rand` gives floats between 0 and 1, `randint(low, high, size)` gives integers from `low` up to but not including `high`, and `uniform(low, high, size)` gives floats between two values.

```python {.marimo}
np.random.seed(0)
array_eighteen = np.random.rand(3, 4)
print(array_eighteen, array_eighteen.dtype)

array_eighteen = np.random.randint(3, 5)
print(array_eighteen)

array_eighteen = np.random.randint(3, 5, 10)
print(array_eighteen)

array_eighteen = np.random.randint(3, 5, (10, 5))
print(array_eighteen)
```

```python {.marimo}
array_nineteen = np.random.uniform(3, 10, (3, 4))
print(array_nineteen, array_nineteen.dtype)
```

## Ranges: arange, linspace and logspace
- `np.arange(start, stop, step)` works like `range` but returns an array
- `np.linspace(start, stop, count)` gives `count` evenly spaced values, including the stop value
- `np.logspace(start, stop, count)` gives values spaced evenly on a log scale (powers of 10 by default)

The `reshape` method changes the shape of an array without changing its values; it is explained in the next lesson.

```python {.marimo}
# array creation with range function
array_twenty = np.arange(2, 20, 2)
print(array_twenty, array_twenty.dtype, array_twenty.size)

array_twenty = array_twenty.reshape(3, 3)
print(array_twenty, array_twenty.dtype, array_twenty.size)

# array creation with linspace (linear space)
array_twenty_one = np.linspace(2, 20, 5, retstep=False)
print(array_twenty_one, array_twenty_one.dtype, array_twenty_one.shape)

# array creation with logspace
array_twenty_two = np.logspace(0, 4, 5)
print(array_twenty_two)
```

## Matrices for linear algebra
`np.diag` puts a list on the diagonal of a square matrix. `np.eye(rows, columns, k)` creates ones on a diagonal and zeros elsewhere; `k` shifts the diagonal (negative is below the main one).

```python {.marimo}
array_twenty_three = np.diag([1, 2, 3, 4, 5])
print(array_twenty_three)

array_twenty_four = np.eye(4, dtype=np.int64)
print(array_twenty_four)

array_twenty_four = np.eye(3, 4, dtype=np.int64)
print(array_twenty_four)

array_twenty_four = np.eye(3, 4, -1, dtype=np.int64)
print(array_twenty_four)
```