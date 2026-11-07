---
title: Functions
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Return Values
The `return` statement sends a result from a function back to the code that called it. You will learn how to use returned values in calculations, how a function can return several values at once, and how to unpack them.
<!---->
## Returning a value
Unlike `print`, which only shows something on the screen, `return` hands a value back so the caller can store it or keep calculating with it. A function stops as soon as it reaches `return`.

```python {.marimo}
def sqr_summations(a, b, c):
    print(f"a={a} | b={b} | c={c}")
    summations = a**2 + b**2 + c**2
    return summations


ans = sqr_summations(10, 20, 30) + 10
print(ans)
```

## What type comes back?
A function can return any type of value. Use `type()` to see what you got.

```python {.marimo}
def return_number():
    return 10


def return_text():
    return "name"


print(type(return_number()))
print(type(return_text()))
```

## Returning a list
Returning one list gives you a list back. A list is an ordered collection written inside square brackets. Lists are covered in detail in Lesson 05.

```python {.marimo}
def return_list():
    numbers = [10, 20, 30]
    return numbers


values = return_list()
print(type(values), values)
```

## Returning multiple values
When you write several values after `return` separated by commas, Python packs them together into one **tuple** (a fixed group of values written in parentheses). The caller can **unpack** the tuple into separate variables in one line.

```python {.marimo}
def return_three():
    return 10, 20, 30


packed = return_three()
print(type(packed), packed)

first, second, third = return_three()  # unpacking
print(first, second, third)
```

The same happens when the returned values are lists: returning one list gives a list, but returning two lists gives a tuple that holds both lists.

```python {.marimo}
def return_two_lists():
    ints = [10, 20, 30]
    floats = [10.1, 20.1, 30.1]
    return ints, floats


both = return_two_lists()
print(f"type: {type(both)} and value: {both}")

int_list, float_list = return_two_lists()
print(int_list, float_list)
```

The values do not need to be of the same type. Any mix can be returned together and unpacked.

```python {.marimo}
def return_mixed():
    return "Python", 3, [1, 2, 3]


language, number, items = return_mixed()
print(language, number, items)
```

## A function without return
If a function never reaches a `return` statement, it returns `None` automatically.

```python {.marimo}
def no_return():
    x = 5


print(no_return())
```