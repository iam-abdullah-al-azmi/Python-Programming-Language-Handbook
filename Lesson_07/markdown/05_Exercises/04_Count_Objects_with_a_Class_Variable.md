---
title: Classes and Objects Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Create a Student class that keeps count of how many objects were created in a class variable, and a class method that returns this count.

```python {.marimo hide_code="true"}
class Student:
    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

    @classmethod
    def get_total_students(cls):
        return cls.total_students

Student("Rafi")
Student("Mim")
Student("Karim")
print(f"Total students: {Student.get_total_students()}")
```