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
        Exercise 03: Create a Person class with a class method from_string() that builds an object from a string like 'Azmi-22', and a static method that checks whether an age is valid (between 0 and 120) and is used inside the constructor.
    """)
    return


@app.cell
def _():
    class Person:
        def __init__(self, name, age):
            if not Person.is_valid_age(age):
                raise ValueError(f"Invalid age: {age}")
            self.name = name
            self.age = age

        @classmethod
        def from_string(cls, text):
            name, age = text.split("-")
            return cls(name, int(age))

        @staticmethod
        def is_valid_age(age):
            return 0 <= age <= 120


    person = Person.from_string("Azmi-22")
    print(f"Name: {person.name} | Age: {person.age}")

    try:
        Person.from_string("Ghost-500")
    except ValueError as error:
        print(error)
    return


if __name__ == "__main__":
    app.run()
