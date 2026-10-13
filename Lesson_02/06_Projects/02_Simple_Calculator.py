import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Projects")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Project 02: Simple Calculator
    Take two numbers and a choice from the user, then add, subtract, multiply or divide the numbers accordingly.
    """)
    return


@app.cell
def _():
    first_number = eval(input("Enter the first number: "))
    second_number = eval(input("Enter the second number: "))

    return (first_number, second_number)


@app.cell
def _():
    print(
        "Which operation you want? | (1) Addition | (2) Subtraction | (3) Multiplication | (4) Division"
    )
    return


@app.cell
def _():
    choice = eval(input("Give your choice: "))

    return (choice,)


@app.cell
def _(choice, first_number, second_number):
    if choice == 1:
        print(
            f"First number is: {first_number} | Second number is: {second_number} | Addition: {first_number + second_number}"
        )
    elif choice == 2:
        print(
            f"First number is: {first_number} | Second number is: {second_number} | Subtraction: {first_number - second_number}"
        )
    elif choice == 3:
        print(
            f"First number is: {first_number} | Second number is: {second_number} | Multiplication: {first_number * second_number}"
        )
    elif choice == 4:
        if second_number != 0:
            print(
                f"First number is: {first_number} | Second number is: {second_number} | Division: {first_number / second_number}"
            )
        else:
            print("Denominator can't be zero")
    else:
        print("Wrong input!!!")
    return


if __name__ == "__main__":
    app.run()
