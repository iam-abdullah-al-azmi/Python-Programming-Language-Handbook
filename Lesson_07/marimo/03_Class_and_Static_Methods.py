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
    # Class and Static Methods
    A class can have three kinds of methods: instance methods, class methods and static methods. You will learn what each one receives and when to use it.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Reference: [Python Class Method vs Static Method vs Instance Method](https://realpython.com/instance-class-and-static-methods-demystified/)

    - An instance method receives the object as `self` and can use both the object's data and the class.
    - A class method is marked with `@classmethod`, receives the class as `cls` and can use the class's data.
    - A static method is marked with `@staticmethod`, receives neither `self` nor `cls`, and is just a normal function placed inside the class.
    """)
    return


@app.cell
def _():
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
    return (DemoClass,)


@app.cell
def _(mo):
    mo.md(r"""
    An instance method needs an object, so calling it through the class alone does not work. Class and static methods can be called directly on the class, without creating any object.
    """)
    return


@app.cell
def _(DemoClass):
    print(DemoClass.class_method())
    print(DemoClass.static_method())

    try:
        DemoClass.instance_method()
    except TypeError as _error:
        print(f"TypeError: {_error}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Static methods
    Use a static method for a utility function that is related to the class but does not need any object or class data, such as a conversion or a validation.
    """)
    return


@app.cell
def _():
    class Temperature:
        @staticmethod
        def celsius_to_fahrenheit(celsius):
            return celsius * 9 / 5 + 32


    print(Temperature.celsius_to_fahrenheit(0))
    print(Temperature.celsius_to_fahrenheit(100))
    return


@app.cell
def _():
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
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Class methods
    A class method works with the class itself. Its most common use is an alternative constructor: a second way to build an object, here from a string such as `"Azmi-22"`. Because it receives `cls`, it also works for subclasses.
    """)
    return


@app.cell
def _():
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
    return


@app.cell
def _(mo):
    mo.md(r"""
    A class method can also read and change data that is shared by the whole class. The next notebook explains such class variables in detail.
    """)
    return


@app.cell
def _():
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
    return


if __name__ == "__main__":
    app.run()
