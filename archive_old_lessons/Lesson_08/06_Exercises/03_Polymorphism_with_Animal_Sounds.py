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
        Exercise 03: Create Dog, Cat and Cow classes that each have a sound() method. Loop over objects of all three classes and call the same method on each.
    """)
    return


@app.cell
def _():
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
    return


if __name__ == "__main__":
    app.run()
