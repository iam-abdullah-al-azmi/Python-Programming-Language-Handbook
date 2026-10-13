import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="OOP Principles Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 01: Create an Employee class and a Manager class that inherits from it and adds a team size. Use super() to reuse the parent's constructor.
    """)
    return


@app.cell
def _():
    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

        def info(self):
            print(f"Name: {self.name} | Salary: {self.salary}")


    class Manager(Employee):
        def __init__(self, name, salary, team_size):
            super().__init__(name, salary)
            self.team_size = team_size

        def info(self):
            print(f"Name: {self.name} | Salary: {self.salary} | Team Size: {self.team_size}")


    employee = Employee("Karim", 30000)
    manager = Manager("Salma", 60000, 5)
    employee.info()
    manager.info()
    return


if __name__ == "__main__":
    app.run()
