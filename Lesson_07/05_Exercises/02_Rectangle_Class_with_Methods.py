import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Classes and Objects")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 02: Create a Rectangle class with a constructor that takes length and width, and methods that return its area and perimeter. Create two rectangles and print the results.
    """)
    return


@app.cell
def _():
    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width

        def perimeter(self):
            return 2 * (self.length + self.width)


    rectangle_one = Rectangle(4, 5)
    rectangle_two = Rectangle(10, 3)
    print(f"Area: {rectangle_one.area()} | Perimeter: {rectangle_one.perimeter()}")
    print(f"Area: {rectangle_two.area()} | Perimeter: {rectangle_two.perimeter()}")
    return


if __name__ == "__main__":
    app.run()
