import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="OOP Principles")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Abstraction
    Abstraction hides the details and shows only what an object must provide. You will learn to write an abstract class whose abstract methods every child class has to implement.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Abstract classes
    A class that inherits from `ABC` and has at least one method marked with `@abstractmethod` is an abstract class. It describes what its children must do, but it leaves the details to them. We cannot create an object of an abstract class, and a child that does not implement all the abstract methods is abstract too.
    """)
    return


@app.cell
def _():
    from abc import ABC, abstractmethod


    class Telephone(ABC):
        @abstractmethod
        def make_call(self):
            pass


    class Sphone(Telephone):
        def make_call(self):
            print("Making a call using SPhone")


    class Iphone(Telephone):
        def make_call_one(self):  # make_call is not implemented
            print("Making a call using IPhone")
    return ABC, Iphone, Sphone, Telephone, abstractmethod


@app.cell
def _(Iphone, Sphone, Telephone):
    sp = Sphone()
    sp.make_call()

    try:
        Telephone()
    except TypeError as _error:
        print(f"TypeError: {_error}")

    try:
        Iphone()
    except TypeError as _error:
        print(f"TypeError: {_error}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Another example: shapes
    An abstract `Shape` class promises an `area()` method. Each child class implements it differently, and all of them can be used the same way.
    """)
    return


@app.cell
def _(ABC, abstractmethod):
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


    for _shape in (Rectangle(4, 5), Circle(2)):
        print(f"{type(_shape).__name__} area: {_shape.area()}")
    return


if __name__ == "__main__":
    app.run()
