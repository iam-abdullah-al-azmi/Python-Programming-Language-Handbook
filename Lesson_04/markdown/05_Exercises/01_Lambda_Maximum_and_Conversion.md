---
title: Functional Tools and Generators Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Write a lambda function that converts a temperature from Celsius to Fahrenheit (F = C * 9 / 5 + 32) and another lambda that returns the larger of two numbers.

```python {.marimo hide_code="true"}
to_fahrenheit = lambda c: c * 9 / 5 + 32
larger = lambda a, b: a if a > b else b

print(to_fahrenheit(0))
print(to_fahrenheit(100))
print(larger(8, 15))
print(larger(-3, -9))
```