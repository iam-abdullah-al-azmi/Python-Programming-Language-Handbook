---
title: Tuples, Sets and Dictionaries Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Merge two dictionaries into a new one (the value from the second dictionary wins for a repeated key), then use a dictionary of student marks to print the average mark of one student with two decimal places.

```python {.marimo hide_code="true"}
first = {"a": 1, "b": 2, "c": 3}
second = {"c": 30, "d": 40}
merged = {}
for key, value in first.items():
    merged[key] = value
for key, value in second.items():
    merged[key] = value
print(merged)
print(merged == first | second)
```

```python {.marimo hide_code="true"}
student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60],
}
query_name = "Malika"
marks = student_marks[query_name]
average = sum(marks) / len(marks)
print(f"{query_name}: {average:.2f}")
```