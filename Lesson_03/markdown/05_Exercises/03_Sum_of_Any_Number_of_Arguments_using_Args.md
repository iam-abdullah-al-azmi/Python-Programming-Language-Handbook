---
title: Functions Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Write a function using *args that returns the sum of any number of values passed to it. Then use a global counter to count how many times the function has been called.

```python {.marimo hide_code="true"}
call_count = 0

def add_all(*args):
    global call_count
    call_count += 1
    total = 0
    for value in args:
        total += value
    return total

print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40, 50))
print(f"add_all was called {call_count} times")
```