---
title: Functional Tools and Generators Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Write a generator function that yields the even numbers up to a given limit, and use next() and a for loop to read values from it.

```python {.marimo hide_code="true"}
def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number

evens = even_numbers(10)
print(next(evens))
print(next(evens))
for number in evens:
    print(number, end=" ")
print()
```