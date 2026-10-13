import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Fundamental")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 04: Create an abstract Shape class with an abstract area() method. Implement it in Rectangle and Circle classes (use 3.14 for pi) and print the areas.
    """)
    return


@app.cell
def _():
    from abc import ABC, abstractmethod

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

    class Rectangle(Shape):
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius**2

    for shape in (Rectangle(4, 5), Circle(2)):
        print(f"{type(shape).__name__} area: {shape.area()}")

    try:
        Shape()
    except TypeError as error:
        print(f"Cannot create an abstract class object: {error}")
    return


if __name__ == "__main__":
    app.run()
