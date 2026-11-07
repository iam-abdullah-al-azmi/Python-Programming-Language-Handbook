---
title: Strings and Lists
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Lists
A list is an ordered, changeable collection of items written inside square brackets. You will learn how to create lists, read items by index, slice them, change them and store different types, including lists inside lists.
<!---->
## Creating a list and indexing
Items are separated by commas. Like in strings, the first item has index 0.

```python {.marimo}
numbers = [4, 2, 9, 1, 5, 6]
print(numbers, type(numbers))
print(len(numbers))

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])
```

## Negative indexing
Negative indexes count from the end, so `-1` is the last item and `-6` is the first item of a six-item list.

```python {.marimo}
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])
print(numbers[-5])
print(numbers[-6])
```

## Looping over a list
You can loop over the positions with `range(len(...))`, or loop directly over the items.

```python {.marimo}
for _i in range(len(numbers)):
    print(numbers[_i], end=" ")
print()

for _num in numbers:
    print(_num, end=" ")
```

## Lists are mutable
Unlike strings, a list can be changed after it is created by assigning to one of its positions.

```python {.marimo}
scores = [4, 2, 9, 1, 5, 6]
print(scores)
scores[0] = 10
print(scores)

scores[2] = scores[2] * scores[1]
print(scores)
```

## Slicing
Slicing works exactly like it does for strings: the result is a new list.

```python {.marimo}
print(numbers[1:4])  # from index 1 to index 3
print(numbers[2:])  # from index 2 to the end
print(numbers[:4])  # from the start to index 3
print(numbers[::2])  # every second item
print(numbers[::-1])  # the whole list backwards
```

## Joining, repeating and checking membership
`+` joins two lists, `*` repeats a list, and `in` checks whether an item is present.

```python {.marimo}
print([1, 2, 3] + [4, 5])
print([0] * 5)
print(9 in numbers)
print(100 in numbers)
```

## Lists can hold any type
A list can contain floats, strings or a mixture of types. `type()` shows what each item is.

```python {.marimo}
_float_numbers = [4.5, 2.3, 9.1, 1.0, 5.6, 6.2]

for _num in _float_numbers:
    print(_num, type(_num), "|", end=" ")
```

```python {.marimo}
_string_list = ["apple", "banana", "cherry", "date"]

for _fruit in _string_list:
    print(_fruit, type(_fruit), "|", end=" ")
```

```python {.marimo}
mixed_list = [1, 2.5, "hello", True, 3 + 4j]

for item in mixed_list:
    print(item, type(item), "|", end=" ")
```

## Nested lists
A list can contain other lists. Use one index for the inner list and a second index for the item inside it.

```python {.marimo}
nested_list = [[1, 2], [3.5, 4.5], ["a", "b", "c"], [True, False], [5 + 6j, 7 + 8j]]

for _sublist in nested_list:
    for _element in _sublist:
        print(_element, type(_element), "|", end=" ")
    print(_sublist, type(_sublist), "|", end="\n")

print(nested_list[2][1])
```