---
title: Conditionals and Loops
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Nested Loops and Pattern Printing
In this notebook you will put one loop inside another and use it to print number, letter and symbol patterns. The outer loop controls the rows and the inner loop controls the columns.
<!---->
## How nested loops run
For every single round of the outer loop, the inner loop runs completely. Calling print() with nothing inside moves the output to the next line. In each pattern below the size is fixed; the original notebook read it with `int(input("Enter the no"))`.

```python {.marimo}
for _i in range(1, 4):
    for _k in range(1, 4):
        print(f"{_i}x{_k}", end="  ")
    print()
```

## Number triangle
Row i prints the numbers from 1 to i.

```python {.marimo}
_user_want = 5  # int(input("Enter the no"))

for _i in range(1, _user_want + 1):
    for _k in range(1, _i + 1):
        print(f"{_k}", end="")

    print()
```

## Continuing number triangle
A counter outside the loops keeps increasing, so the numbers continue from row to row.

```python {.marimo}
_user_want = 5
_count = 1

for _i in range(1, _user_want + 1):
    for _k in range(1, _i + 1):
        print(f"{_count}", end="")
        _count += 1

    print()
```

## Inverted number triangle
Counting the outer loop downwards makes the rows shorter.

```python {.marimo}
_user_want = 5

for _i in range(_user_want, 0, -1):
    for _k in range(1, _i + 1):
        print(f"{_k}", end="")

    print()
```

## Letter triangle
The chr function turns an ASCII code into a letter, so the pattern continues A, B, C, ...

```python {.marimo}
_user_want = 5
_letter = 65

for _i in range(1, _user_want + 1):
    for _k in range(1, _i + 1):
        print(f"{chr(_letter)}", end="")
        _letter += 1

    print()
```

## Hollow square pattern
Print the symbol only in the first and last row and the first and last column; print a space elsewhere.

```python {.marimo}
_user_input = 6

for _i in range(1, _user_input + 1):
    for _k in range(1, _user_input + 1):
        if _i == 1 or _i == _user_input or _k == 1 or (_k == _user_input):
            print("+", end=" ")
        else:
            print(" ", end=" ")

    print()
```

## Inverted and rotated half-pyramid
Each row first prints some spaces and then the symbols; the spaces decrease while the symbols increase.

```python {.marimo}
_user_input = 5

for _i in range(1, _user_input + 1):
    _n = _user_input - _i
    for _k in range(1, _n + 1):
        print(" ", end=" ")
    for _k in range(1, _i + 1):
        print("+", end=" ")

    print()
```

## Pyramid
Row i has `n - i` spaces and `2 * i - 1` symbols.

```python {.marimo}
_user_input = 5

for _i in range(1, _user_input + 1):
    _num_spaces = _user_input - _i
    for _k in range(
        1, _num_spaces + 1
    ):  # no of spaces decrease as the row no increases
        print(" ", end=" ")
    _num_symbols = 2 * _i - 1
    for _k in range(1, _num_symbols + 1):
        print("+", end=" ")

    print()
```