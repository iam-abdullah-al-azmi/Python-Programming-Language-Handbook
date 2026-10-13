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
        Exercise 03: Create a class that keeps count of how many objects were created in a class variable, and a class method that returns this count.
    """)
    return


@app.cell
def _():
    class Student:
        total_students = 0

        def __init__(self, name):
            self.name = name
            Student.total_students += 1

        @classmethod
        def get_total_students(cls):
            return cls.total_students

    Student("Rafi")
    Student("Mim")
    Student("Karim")
    print(f"Total students: {Student.get_total_students()}")
    return


if __name__ == "__main__":
    app.run()
