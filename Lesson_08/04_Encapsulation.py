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
    # Encapsulation
    Encapsulation hides the data inside a class and controls how the outside code can reach it. You will learn public, protected and private attributes, getters and setters, and the `@property` decorator.

    - Encapsulation means bundling the data (attributes) and the methods that work on that data inside a class, and controlling how the outside world can reach the data.
    - Python has no real "private" keyword. It uses naming conventions instead:
        - `name` ----> public, can be used anywhere
        - `_name` ----> protected, a convention that says "use inside the class or its subclasses only"
        - `__name` ----> private, Python renames it internally (name mangling) so it is hard to reach from outside
    """)
    return


@app.cell
def _():
    # Public, protected and private attributes
    class Student:
        def __init__(self, name, roll, cgpa):
            self.name = name  # public
            self._roll = roll  # protected (only a convention)
            self.__cgpa = cgpa  # private (name mangled)

        def show(self):
            print(f"Name: {self.name} | Roll: {self._roll} | CGPA: {self.__cgpa}")

    student = Student("Azmi", 101, 3.8)
    student.show()

    print(student.name)  # works
    print(student._roll)  # works, but we should not do this
    try:
        print(student.__cgpa)
    except AttributeError as error:
        print(f"AttributeError: {error}")
    return (student,)


@app.cell
def _(student):
    # Name mangling: __cgpa is stored as _Student__cgpa, so it is hidden, not truly locked
    print(student.__dict__)
    print(student._Student__cgpa)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Getter and setter methods
    - Instead of letting the outside code change a private attribute directly, we give it a method that can check the new value first.
    """)
    return


@app.cell
def _():
    class BankAccount:
        def __init__(self, owner, balance):
            self.owner = owner
            self.__balance = balance

        def get_balance(self):  # getter
            return self.__balance

        def set_balance(self, amount):  # setter with validation
            if amount >= 0:
                self.__balance = amount
            else:
                print("Balance cannot be negative!")

    account = BankAccount("Azmi", 1000)
    account.set_balance(1500)
    account.set_balance(-50)
    print(account.get_balance())
    return


@app.cell
def _(mo):
    mo.md(r"""
    The @property decorator
    - `@property` lets us use a getter and a setter like a normal attribute, which is the more Pythonic way.
    """)
    return


@app.cell
def _():
    class Circle:
        def __init__(self, radius):
            self.__radius = radius

        @property
        def radius(self):  # getter
            return self.__radius

        @radius.setter
        def radius(self, value):  # setter
            if value > 0:
                self.__radius = value
            else:
                print("Radius must be positive!")

        @property
        def area(self):  # read-only attribute, there is no setter
            return 3.14159 * self.__radius**2

    circle = Circle(5)
    print(circle.radius, circle.area)

    circle.radius = 10
    print(circle.radius, circle.area)

    circle.radius = -3
    print(circle.radius)

    try:
        circle.area = 100
    except AttributeError as error:
        print(f"AttributeError: {error}")
    return


if __name__ == "__main__":
    app.run()
