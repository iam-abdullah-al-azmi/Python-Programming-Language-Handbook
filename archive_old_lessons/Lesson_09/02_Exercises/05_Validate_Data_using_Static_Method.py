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
        Exercise 05: Create a class with a static method that checks whether an age is valid (between 0 and 120), and use it inside the constructor.
    """)
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
    except ValueError as error:
        print(error)
    return


if __name__ == "__main__":
    app.run()
