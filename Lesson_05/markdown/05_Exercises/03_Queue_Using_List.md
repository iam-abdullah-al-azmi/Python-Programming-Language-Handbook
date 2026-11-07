---
title: Strings and Lists Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Use a list as a queue: add three people to the line, then serve them one by one (first in, first out).

```python {.marimo hide_code="true"}
queue = []
queue.append("Rafi")
queue.append("Mim")
queue.append("Sakib")
print(f"Queue: {queue}")
while len(queue) > 0:
    print(f"Serving: {queue.pop(0)} | Remaining: {queue}")
```