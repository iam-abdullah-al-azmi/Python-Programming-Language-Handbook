---
title: Tuples, Sets and Dictionaries Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Count how many times each word appears in a sentence using a dictionary, then print its keys, values and items.

```python {.marimo hide_code="true"}
sentence = "the cat and the dog and the bird"
frequency = {}
for word in sentence.split():
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)
```

```python {.marimo hide_code="true"}
print(f"Keys: {list(frequency.keys())}")
print(f"Values: {list(frequency.values())}")
for key, value in frequency.items():
    print(f"{key} -> {value}")
```