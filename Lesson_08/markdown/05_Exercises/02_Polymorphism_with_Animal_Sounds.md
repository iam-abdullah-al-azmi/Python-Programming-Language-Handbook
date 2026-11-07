---
title: OOP Principles Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Create Dog, Cat and Cow classes that each have a sound() method. Loop over objects of all three classes and call the same method on each.

```python {.marimo hide_code="true"}
class Dog:
    def sound(self):
        return "Woof"

class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

for animal in (Dog(), Cat(), Cow()):
    print(f"{type(animal).__name__} says {animal.sound()}")
```