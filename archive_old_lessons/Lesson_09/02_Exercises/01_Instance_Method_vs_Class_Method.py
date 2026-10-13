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
        Exercise 01: Create a class with an instance method and a class method. Call the instance method using an object and the class method using the class itself.
    """)
    return


@app.cell
def _():
    class Counter:
        def instance_method(self):
            return ("instance method called", self.__class__.__name__)

        @classmethod
        def class_method(cls):
            return ("class method called", cls.__name__)

    counter = Counter()
    print(counter.instance_method())
    print(Counter.class_method())
    return


if __name__ == "__main__":
    app.run()
