---
title: Functions Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Write a recursive function power(base, exponent) that computes base raised to a non-negative whole exponent without using the ** operator, and a recursive function that returns the n-th Fibonacci number.

```python {.marimo hide_code="true"}
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(power(2, 10))
print(power(5, 3))
print(fibonacci(10))
```