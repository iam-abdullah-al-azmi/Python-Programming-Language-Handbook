---
title: OOP Principles Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 01: Create an Employee class and a Manager class that inherits from it and adds a team size. Use super() to reuse the parent's constructor.

```python {.marimo hide_code="true"}
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
        print(
            f"Name: {self.name} | Salary: {self.salary} | Team Size: {self.team_size}"
        )

employee = Employee("Karim", 30000)
manager = Manager("Salma", 60000, 5)
employee.info()
manager.info()
```