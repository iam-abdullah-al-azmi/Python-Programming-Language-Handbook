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
        Exercise 04: Create a Person class with a class method from_string() that builds an object from a string like 'Azmi-22'.
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


if __name__ == "__main__":
    app.run()
