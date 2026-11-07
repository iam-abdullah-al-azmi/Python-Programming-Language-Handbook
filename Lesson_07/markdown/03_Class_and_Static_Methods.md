---
title: Classes and Objects
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Class and Static Methods
A class can have three kinds of methods: instance methods, class methods and static methods. You will learn what each one receives and when to use it.
<!---->
Reference: [Python Class Method vs Static Method vs Instance Method](https://realpython.com/instance-class-and-static-methods-demystified/)

- An instance method receives the object as `self` and can use both the object's data and the class.
- A class method is marked with `@classmethod`, receives the class as `cls` and can use the class's data.
- A static method is marked with `@staticmethod`, receives neither `self` nor `cls`, and is just a normal function placed inside the class.

```python {.marimo}
class DemoClass:
    def instance_method(self):
        return ("instance method called", self)

    @classmethod
    def class_method(cls):
        return ("class method called", cls)

    @staticmethod
    def static_method():
        return ("static method called",)


obj = DemoClass()
print(obj.instance_method())
print(obj.class_method())
print(obj.static_method())
```

An instance method needs an object, so calling it through the class alone does not work. Class and static methods can be called directly on the class, without creating any object.

```python {.marimo}
print(DemoClass.class_method())
print(DemoClass.static_method())

try:
    DemoClass.instance_method()
except TypeError as _error:
    print(f"TypeError: {_error}")
```

## Static methods
Use a static method for a utility function that is related to the class but does not need any object or class data, such as a conversion or a validation.

```python {.marimo}
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32


print(Temperature.celsius_to_fahrenheit(0))
print(Temperature.celsius_to_fahrenheit(100))
```

```python {.marimo}
class User:
    def __init__(self, name, age):
        if not User.is_valid_age(age):
            raise ValueError(f"Invalid age: {age}")
        self.name = name
        self.age = age

    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 120


user = User("Azmi", 22)
print(f"Created user {user.name}, age {user.age}")

try:
    User("Ghost", 500)
except ValueError as _error:
    print(_error)
```

## Class methods
A class method works with the class itself. Its most common use is an alternative constructor: a second way to build an object, here from a string such as `"Azmi-22"`. Because it receives `cls`, it also works for subclasses.

```python {.marimo}
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text):
        name, age = text.split("-")
        return cls(name, int(age))


person = Person.from_string("Azmi-22")
print(f"Name: {person.name} | Age: {person.age}")
```

A class method can also read and change data that is shared by the whole class. The next notebook explains such class variables in detail.

```python {.marimo}
class Counter:
    total = 0

    def __init__(self):
        Counter.total += 1

    @classmethod
    def get_total(cls):
        return cls.total


Counter()
Counter()
Counter()
print(f"Objects created: {Counter.get_total()}")
```