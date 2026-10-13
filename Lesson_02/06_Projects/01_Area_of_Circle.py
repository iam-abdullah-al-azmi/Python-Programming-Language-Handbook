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
    # Project 01: Calculate the Area of a Circle
    Take the radius of a circle from the user and calculate its area with the formula pi * r**2, handling a zero and a negative radius.
    """)
    return


@app.cell
def _():
    from math import pi

    return (pi,)


@app.cell
def _():
    radius = eval(input("Enter the radius of the circle: "))

    return (radius,)


@app.cell
def _(pi, radius):
    if not isinstance(radius, (int, float)):
        print("Error: Radius must be a number!")
    elif radius > 0:
        area = pi * (radius**2)
        print(f"Radius of the circle: {radius} | Area: {area:.2f}")
    elif radius == 0:
        print("A circle with radius 0 has no area.")
    else:
        print("Error: Radius cannot be negative!")
    return


if __name__ == "__main__":
    app.run()
