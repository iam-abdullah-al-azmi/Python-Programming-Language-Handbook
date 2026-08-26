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
        Excercise 02: Take the user input of age, height, and name and print it. Use the try-except block to handle invalid input.
    """)


@app.cell
def _():
    try:
        age = int(input("Enter your age: "))
        height = float(input("Enter your height: "))
        name = input("Enter your name: ")
        age = 10
        height = 5.8
        name = "abcd"

        print(f"Name: {name} | Age: {age} | Height: {height}")

    except ValueError:
        print("Invalid error!")
    return


if __name__ == "__main__":
    app.run()
