---
title: OOP Principles
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Inheritance
Inheritance lets a new class (the child) reuse the attributes and methods of an existing class (the parent). You will learn how to create a child class, call the parent with `super()` and override methods.
<!---->
## A parent class
First we write a normal class. It will become the parent class.

```python {.marimo}
class Table:
    def __init__(self, length, width, material, diameter, cross_section) -> None:
        self.length = length
        self.width = width
        self.material = material
        self.diameter = diameter
        self.cross_section = cross_section

    def table_info(self):
        print(f"Table Info:\nLength: {self.length} | Width: {self.width} | Material: {self.material} | Diameter: {self.diameter} | Cross Section: {self.cross_section}")


table_one = Table(23, 12, "Wood", 3, 43)
table_one.table_info()
```

## A child class
We write the parent class in brackets after the child class name. The child gets every attribute and method of the parent. `super().__init__()` calls the parent's constructor, so we do not repeat its code, and then the child adds its own attributes. If the child defines a method with the same name as the parent's, it overrides the parent's version.

```python {.marimo}
class SofaTable(Table):
    def __init__(self, length, width, material, diameter, cross_section, style, glass) -> None:
        super().__init__(length, width, material, diameter, cross_section)

        self.style = style
        self.glass = glass

    def table_info(self):  # overrides the parent's method
        print(f"Table Info:\nLength: {self.length} | Width: {self.width} | Material: {self.material} | Diameter: {self.diameter} | Cross Section: {self.cross_section} | Style: {self.style} | Glass: {self.glass}")


table_two = SofaTable(23, 12, "Wood", 3, 43, "abcd", True)
table_two.table_info()
```

## Checking the relationship
`isinstance()` tells whether an object belongs to a class (or to one of its parents), and `issubclass()` checks the relationship between two classes. A child object can use every method that its parent has.

```python {.marimo}
print(isinstance(table_two, SofaTable), isinstance(table_two, Table))
print(isinstance(table_one, SofaTable))
print(issubclass(SofaTable, Table))
```

## Reusing a method with super()
Inside an overriding method, `super().method()` runs the parent's version first, and the child can then add more to it. This is shorter than copying the parent's code.

```python {.marimo}
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"Name: {self.name} | Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def info(self):
        super().info()
        print(f"Team Size: {self.team_size}")


Employee("Karim", 30000).info()
Manager("Salma", 60000, 5).info()
```

## Multilevel inheritance
A child class can itself be the parent of another class. The grandchild inherits from both the child and the grandparent.

```python {.marimo}
class Animal:
    def eat(self):
        return "eating"


class Dog(Animal):
    def bark(self):
        return "barking"


class Puppy(Dog):
    def play(self):
        return "playing"


puppy = Puppy()
print(puppy.eat(), puppy.bark(), puppy.play())
print(issubclass(Puppy, Animal))
```