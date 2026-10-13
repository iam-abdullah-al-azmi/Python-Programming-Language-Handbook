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
    Project 01: Calculate the Area of a Circle
    """)
    return


@app.cell
def _():
    radius = eval(input("Enter the radius of the circle: "))
    return (radius,)


@app.cell
def _(pi, radius):
    if radius > 0:
        area = pi * (radius**2)
        print(
            f"Radius of the circle: {radius} | Area: {area} | Data Type: {isinstance(radius, int)}"
        )
    elif radius == 0:
        print("A circle with radius 0 has no area.")
    else:
        print("Error: Radius cannot be negative or string!")
    return


if __name__ == "__main__":
    app.run()
