---
title: Classes and Objects Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Create a Student class with name and marks attributes and a method that prints the student's information. Create two objects and call the method.

```python {.marimo hide_code="true"}
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def info(self):
        print(f"Name: {self.name} | Marks: {self.marks}")

student_one = Student("Rafi", 85)
student_two = Student("Mim", 92)
student_one.info()
student_two.info()
```