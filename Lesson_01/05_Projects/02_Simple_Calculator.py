import marimo

__generated_with = "0.23.14"
app = marimo.App()


@app.cell
def _():
    from math import pi

    import marimo as mo

    return mo, pi


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project 02: Simple calculator
    """)
    return


@app.cell
def _():
    first_number = eval(input("Enter the first number: "))
    second_number = eval(input("Enter the second number: "))
    return first_number, second_number


@app.cell
def _():
    print(
        f"Which operation you want? | (1) Addition | (2) Subtraction | (3) Multiplication | (4) Division"
    )
    return


@app.cell
def _():
    choice = eval(input("Give your choice: "))
    return (choice,)


@app.cell
def _(choice, first_number, second_number):
    if choice == 1:
        add = first_number + second_number

        print(
            f"First number is: {first_number} | Second number is: {second_number} | Addition: {first_number + second_number}"
        )

    elif choice == 2:
        sub = first_number - second_number

        print(
            f"First number is: {first_number} | Second number is: {second_number} | Subtraction: {first_number - second_number}"
        )

    elif choice == 3:
        mul = first_number * second_number

        print(
            f"First number is: {first_number} | Second number is: {second_number} | Multiplication: {first_number * second_number}"
        )

    elif choice == 4:
        if second_number > 0:
            div = first_number / second_number

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
