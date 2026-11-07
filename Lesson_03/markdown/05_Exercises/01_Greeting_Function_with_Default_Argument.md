---
title: Functions Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Write a function that greets a person by name. If no name is given, it should greet 'Guest' by default.

```python {.marimo hide_code="true"}
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet("Azmi"))
print(greet())
```