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
    # Instance vs Class Variables
    An instance variable belongs to one object, while a class variable is shared by every object of the class. You will learn how to tell them apart and what happens when you change each of them.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Two kinds of variables
    - A class variable is written in the class body, outside any method. It is stored once, on the class.
    - An instance variable is created with `self.name = ...`, usually in `__init__()`. Every object gets its own copy.
    """)
    return


@app.cell
def _():
    class Phone:
        category = "Electronics"  # class variable

        def __init__(self, model, battery, camera, battery_percentage=100):
            self.model = model  # instance variables
            self.battery = battery
            self.camera = camera
            self.battery_percentage = battery_percentage


    apple = Phone("iPhone 15", "3000mAh", "40MPx")
    motorola = Phone("MT-15", "5000mAh", "80MPx", 40)

    print(f"{type(apple)} | {apple.category} | {apple.model} | {apple.camera} | {apple.battery} | {apple.battery_percentage}")
    print(f"{type(motorola)} | {motorola.category} | {motorola.model} | {motorola.camera} | {motorola.battery} | {motorola.battery_percentage}")
    return Phone, apple, motorola


@app.cell
def _(mo):
    mo.md(r"""
    ## Changing a class variable
    When we change a class variable through the class, every object sees the new value, because they all read the same one.
    """)
    return


@app.cell
def _(Phone, apple, motorola):
    Phone.category = "Gadgets"
    print(apple.category, motorola.category, Phone.category)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Assigning through an object creates an instance variable
    If we assign a value through one object, Python does not change the class variable. It creates a new instance variable with the same name on that object, which hides the class variable for that object only.
    """)
    return


@app.cell
def _(Phone, apple, motorola):
    motorola.category = "Super Electronics"

    print(apple.category)  # still the class variable
    print(motorola.category)  # the instance variable hides it
    print(Phone.category)

    print(apple.__dict__.keys())
    print("category" in motorola.__dict__)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## A class variable as a counter
    Because a class variable is shared, it is a good place to store data about all objects together, such as how many objects have been created. We update it through the class name, `Student.total_students`, not through `self`.
    """)
    return


@app.cell
def _():
    class Student:
        total_students = 0

        def __init__(self, name):
            self.name = name
            Student.total_students += 1


    Student("Rafi")
    Student("Mim")
    Student("Karim")
    print(f"Total students: {Student.total_students}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    The wrong way is `self.total_students += 1`. It reads the class value, adds one and then stores the result as a new instance variable, so the shared counter never changes.
    """)
    return


@app.cell
def _():
    class WrongCounter:
        count = 0

        def __init__(self):
            self.count += 1


    WrongCounter()
    wrong_two = WrongCounter()
    print(WrongCounter.count)  # still 0
    print(wrong_two.count)  # 1, a private instance variable
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Mutable class variables are shared
    If a class variable is a list or another mutable object, changing it in place changes it for every object, because nobody creates a new copy. Put a mutable value in `__init__()` when each object needs its own.
    """)
    return


@app.cell
def _():
    class SharedBasket:
        items = []  # one list for the whole class

        def add(self, item):
            self.items.append(item)


    basket_one = SharedBasket()
    basket_two = SharedBasket()
    basket_one.add("apple")
    print(basket_two.items)  # the second basket sees the apple too


    class OwnBasket:
        def __init__(self):
            self.items = []  # one list for each object

        def add(self, item):
            self.items.append(item)


    own_one = OwnBasket()
    own_two = OwnBasket()
    own_one.add("apple")
    print(own_one.items, own_two.items)
    return


if __name__ == "__main__":
    app.run()
