---
title: Strings and Lists Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Take the string 'hello world' and print it in upper case, in title case, reversed, and the number of times the letter 'o' appears in it.

```python {.marimo hide_code="true"}
text = "hello world"
print(text.upper())
print(text.title())
print(text[::-1])
print(f"Number of 'o': {text.count('o')}")
```