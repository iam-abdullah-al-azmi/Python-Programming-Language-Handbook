---
title: Functional Tools and Generators
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Reduce
`reduce()` combines all the items of a collection into one single value by applying a function again and again. You will learn how it works step by step and use it for sums, maximums and products.
<!---->
## `reduce()`
`reduce()` lives in the `functools` module, so it has to be imported first. `reduce(function, iterable)` takes the first two items, passes them to the function, then passes that result together with the third item, and so on until one value is left. The function you give it must accept exactly two arguments, which is a perfect job for a lambda.

```python {.marimo}
from functools import reduce

lst = list(range(2, 34, 3))
print(lst)

summation = reduce(lambda x, y: x + y, lst)
print(summation)
```

## Seeing the steps
Here is what `reduce()` did for a short list `[1, 2, 3, 4]` with addition: `1 + 2 = 3`, then `3 + 3 = 6`, then `6 + 4 = 10`. We can print the steps by using a regular function instead of a lambda.

```python {.marimo}
def add_verbose(x, y):
    print(f"{x} + {y} = {x + y}")
    return x + y


print(reduce(add_verbose, [1, 2, 3, 4]))
```

## Finding the maximum
The function can hold any logic. Here it keeps the bigger of the two values, so after all the steps the biggest one remains.

```python {.marimo}
max_val = reduce(lambda x, y: x if x > y else y, lst)
print(max_val)
```

## Product and an initial value
Multiplying everything together works the same way. `reduce()` also accepts an optional third argument, the **initial value**, which is used as the very first `x`. It is also what is returned for an empty list, so it avoids an error in that case.

```python {.marimo}
numbers = [2, 3, 4, 5]
print(reduce(lambda x, y: x * y, numbers))

print(reduce(lambda x, y: x + y, numbers, 100))
print(reduce(lambda x, y: x + y, [], 0))
```

## Joining strings
`reduce()` is not limited to numbers. Here it joins words into one sentence.

```python {.marimo}
words = ["Python", "is", "fun"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)
```