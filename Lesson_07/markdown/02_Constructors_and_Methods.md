---
title: Classes and Objects
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Constructors and Methods
A constructor sets up every new object with its own data, and a method is a function that belongs to a class. You will learn to write both and to use `self`.
<!---->
## The constructor
The special method `__init__()` runs automatically each time an object is created. Its first parameter, `self`, is the object that is being created, and the other parameters receive the values we pass when we call the class. A parameter can have a default value, so we may leave it out when creating the object.

```python {.marimo}
class Phone:
    def __init__(self, model, battery, camera, battery_percentage=100):
        self.model = model
        self.battery = battery
        self.camera = camera
        self.battery_percentage = battery_percentage


apple = Phone("iPhone 15", "3000mAh", "40MPx")
motorola = Phone("MT-15", "5000mAh", "80MPx", 40)

print(f"{type(apple)} | {apple.model} | {apple.camera} | {apple.battery} | {apple.battery_percentage}")
print(f"{type(motorola)} | {motorola.model} | {motorola.camera} | {motorola.battery} | {motorola.battery_percentage}")
```

## Creating methods
A method is a function defined inside a class. Its first parameter is always `self`, which gives the method access to the attributes of the object it is called on. We call a method with the dot notation, and Python passes `self` for us.

```python {.marimo}
class Book:
    def __init__(self, book_name, page, publication, author) -> None:
        self.book_name = book_name
        self.page = page
        self.publication = publication
        self.author = author

    def book_information(self):  # this is called a method
        print(f"Book name: {self.book_name} | Page: {self.page} | Publication: {self.publication} | Author: {self.author}")


book_one = Book("abcd", 450, "abcd", "abcd")
book_one.book_information()
```

## Methods with parameters and return values
A method can take extra parameters and can return a value, just like a normal function. Calling `Student.method(obj)` is the same as `obj.method()`, which shows what `self` really is.

```python {.marimo}
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def add_marks(self, extra):
        self.marks += extra

    def is_passed(self, pass_mark=40):
        return self.marks >= pass_mark

    def info(self):
        return f"Name: {self.name} | Marks: {self.marks}"


student = Student("Rafi", 35)
print(student.info(), student.is_passed())

student.add_marks(10)  # a method can change the object
print(student.info(), student.is_passed())

print(Student.info(student))  # the same call written explicitly
```

## Methods calling other methods
Inside a class, a method uses `self.method_name()` to call another method of the same object.

```python {.marimo}
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def describe(self):
        return f"{self.length} x {self.width}: area {self.area()}, perimeter {self.perimeter()}"


print(Rectangle(4, 5).describe())
```

## The string representation of an object
Printing an object shows an unhelpful default text. The special method `__str__()` lets us decide what `print()` shows.

```python {.marimo}
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


print(Point(2, 3))
```