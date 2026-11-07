---
title: Classes and Objects Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 02: Create a Rectangle class with a constructor that takes length and width, and methods that return its area and perimeter. Create two rectangles and print the results.

```python {.marimo hide_code="true"}
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle_one = Rectangle(4, 5)
rectangle_two = Rectangle(10, 3)
print(f"Area: {rectangle_one.area()} | Perimeter: {rectangle_one.perimeter()}")
print(f"Area: {rectangle_two.area()} | Perimeter: {rectangle_two.perimeter()}")
```