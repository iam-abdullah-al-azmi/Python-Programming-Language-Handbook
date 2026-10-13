import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Classes and Objects")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Classes and Objects
    A class is a blueprint and an object is a real thing built from that blueprint. In this notebook you will define a simple class, create objects from it and give them attributes.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Defining a class and creating objects
    A class is defined with the `class` keyword. Calling the class like a function creates an object (also called an instance) of it. Every object has the type of the class it was created from.
    """)
    return


@app.cell
def _():
    class Dog:
        pass


    dog_one = Dog()
    dog_two = Dog()

    print(dog_one)
    print(type(dog_one), type(dog_two))
    print(dog_one == dog_two)  # two different objects
    print(isinstance(dog_one, Dog))
    return dog_one, dog_two


@app.cell
def _(mo):
    mo.md(r"""
    ## Attributes
    An attribute is a variable that belongs to an object. We read and change it with the dot notation `object.attribute`. Each object keeps its own attributes, so changing one object does not affect another one.
    """)
    return


@app.cell
def _(dog_one, dog_two):
    dog_one.name = "Rex"
    dog_one.age = 3
    dog_two.name = "Bruno"
    dog_two.age = 5

    print(dog_one.name, dog_one.age)
    print(dog_two.name, dog_two.age)

    dog_one.age = 4  # change an attribute
    print(dog_one.age, dog_two.age)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Class attributes
    An attribute written directly inside the class body belongs to the class and every object can read it. Here the `Phone` class has a `category` attribute that all phones share. The next notebooks show how to give each object its own attributes automatically when it is created.
    """)
    return


@app.cell
def _():
    class Phone:
        category = "Electronics"


    apple = Phone()
    motorola = Phone()

    print(apple.category, motorola.category)
    print(Phone.category)  # can also be read through the class itself
    print(type(apple))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Inspecting an object
    The built-in functions `hasattr()`, `getattr()` and `setattr()` check, read and set an attribute by its name. The `__dict__` attribute shows the attributes that the object itself stores.
    """)
    return


@app.cell
def _(dog_one):
    print(hasattr(dog_one, "name"), hasattr(dog_one, "colour"))
    print(getattr(dog_one, "name"))
    setattr(dog_one, "colour", "brown")
    print(dog_one.__dict__)
    return


if __name__ == "__main__":
    app.run()
