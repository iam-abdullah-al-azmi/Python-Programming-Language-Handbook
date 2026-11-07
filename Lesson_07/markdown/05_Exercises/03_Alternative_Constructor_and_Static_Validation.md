---
title: Classes and Objects Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Create a Person class with a class method from_string() that builds an object from a string like 'Azmi-22', and a static method that checks whether an age is valid (between 0 and 120) and is used inside the constructor.

```python {.marimo hide_code="true"}
class Person:
    def __init__(self, name, age):
        if not Person.is_valid_age(age):
            raise ValueError(f"Invalid age: {age}")
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text):
        name, age = text.split("-")
        return cls(name, int(age))

    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 120

person = Person.from_string("Azmi-22")
print(f"Name: {person.name} | Age: {person.age}")

try:
    Person.from_string("Ghost-500")
except ValueError as error:
    print(error)
```