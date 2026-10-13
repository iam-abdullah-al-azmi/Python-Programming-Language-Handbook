import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Classes and Objects Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 01: Create a Student class with name and marks attributes and a method that prints the student's information. Create two objects and call the method.
    """)
    return


@app.cell
def _():
    class Student:
        def __init__(self, name, marks):
            self.name = name
            self.marks = marks

        def info(self):
            print(f"Name: {self.name} | Marks: {self.marks}")


    student_one = Student("Rafi", 85)
    student_two = Student("Mim", 92)
    student_one.info()
    student_two.info()
    return


if __name__ == "__main__":
    app.run()
