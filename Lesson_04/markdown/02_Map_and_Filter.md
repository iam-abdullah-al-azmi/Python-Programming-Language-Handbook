---
title: Functional Tools and Generators
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Map and Filter
`map()` applies a function to every item of a collection, and `filter()` keeps only the items that pass a test. You will use both with lambda functions to transform and select data.
<!---->
## `map()`
`map(function, iterable)` runs one function on every single value and returns a lazy `map` object. Wrap it in `list()` to see the results. We build the list of odd numbers with `list(range(...))`, where `range(1, 40, 2)` counts from 1 up to 39 in steps of 2.

```python {.marimo}
lst = list(range(1, 40, 2))
print(lst)

sqr = lambda x: x**2
sqr_list = list(map(sqr, lst))
print(sqr_list)
```

The function can also be written directly inside `map()`. Here it uses a conditional expression: even numbers are squared, odd multiples of 3 are cubed, and the rest stay as they are.

```python {.marimo}
sqr_list_cond = list(map(lambda val: val**2 if val % 2 == 0 else (val**3 if val % 3 == 0 else val), lst))
print(sqr_list_cond)
```

## `map()` on a string
A string is a sequence of characters, so `map()` can process it character by character. Passing the existing method `str.upper` as the function converts each character to upper case. `"".join(...)` then glues the characters back into one string.

```python {.marimo}
text = "Hello world, Welcome to the age of artificial intelligence (AI)"

upper_chars = list(map(str.upper, text))
print(upper_chars)

upper_text = "".join(upper_chars)
print(upper_text)
```

## `filter()`
`filter(function, iterable)` is a powerful way to separate data. The function must return `True` or `False` for each item, and only the items that give `True` are kept. First look at what happens if we use `map()` with a test: we get the True/False answers, not the filtered values.

```python {.marimo}
numbers = list(range(2, 50, 2))
print(numbers[-1])

answers = list(map(lambda val: val % 2 == 0, numbers))
print(answers)
```

With `filter()` the numbers that pass the test are kept.

```python {.marimo}
even = list(filter(lambda val: val % 2 == 0, numbers))
print(even)

greater_than_20 = list(filter(lambda val: val > 20, numbers))
print(greater_than_20)
```

## `filter(None, ...)`
If you pass `None` instead of a function, `filter()` removes every value that Python considers false: `0`, `""`, `None`, `False` and empty collections. This is a quick way to clean data.

```python {.marimo}
data = [1, "", None, None, True, False]

cleaned_data = list(filter(None, data))
print(cleaned_data)
```

## `filter()` on a string
Using the upper case string from before, keep only the vowels.

```python {.marimo}
vowels = list(filter(lambda ch: ch in "aAeEiIoOuU", upper_text))
print(vowels)
```

To see each vowel only once, we loop through the result and add a letter only when it is not already in the new list.

```python {.marimo}
unique_vowels = []
for _vowel in vowels:
    if _vowel not in unique_vowels:
        unique_vowels.append(_vowel)
print(unique_vowels)
```

## Using both together
The output of one can feed the next. Here we square every number and then keep only the squares that are bigger than 20.

```python {.marimo}
small = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda v: v**2, small))
big_squares = list(filter(lambda v: v > 20, squares))
print(squares)
print(big_squares)
```