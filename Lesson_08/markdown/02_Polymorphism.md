---
title: OOP Principles
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Polymorphism
Polymorphism means "many forms": the same function or method name works on objects of different types. You will see it in built-in functions, in unrelated classes and in classes that share a parent.
<!---->
## Polymorphism in built-in functions
The built-in `len()` function works on strings, tuples and dictionaries alike.

```python {.marimo}
print(len("Hello World"), len((12, 23, 34)), len({"a": "a", "b": "b"}))
```

## The same method in different classes
The classes below are unrelated, but each has an `info()` method. We can loop over objects of all of them and call `info()` without caring which class each object belongs to. Note the `f` before the string: without it, Python would print the text `{self.brand}` instead of the value.

```python {.marimo}
class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def info(self):
        return f"Brand: {self.brand} and Model: {self.model}"


class Ship:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def info(self):
        return f"Brand: {self.brand} and Model: {self.model}"


class Airplane:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def info(self):
        return f"Brand: {self.brand} and Model: {self.model}"


car_one = Car("abcd", "efgh")
ship_one = Ship("ijkl", "mnop")
airplane_one = Airplane("qrst", "uvwx")

print([item.info() for item in (car_one, ship_one, airplane_one)])
```

## Polymorphism with method overriding
When child classes override a method of a parent class, each child gives its own behaviour for the same method name. The caller just calls `sound()` and every object responds in its own way.

```python {.marimo}
class Animal:
    def sound(self):
        return "some sound"


class Dog(Animal):
    def sound(self):
        return "Woof"


class Cat(Animal):
    def sound(self):
        return "Meow"


class Cow(Animal):
    def sound(self):
        return "Moo"


for _animal in (Animal(), Dog(), Cat(), Cow()):
    print(f"{type(_animal).__name__} says {_animal.sound()}")
```

A function can also use polymorphism: it works with any object that has the method it needs.

```python {.marimo}
def make_sound(animal):
    print(animal.sound())


make_sound(Dog())
make_sound(Cow())
```