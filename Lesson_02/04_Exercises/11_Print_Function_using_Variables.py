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
        Excercise 07: This task is a bit of fun! What you have to do is to print 6 different city names but has to take the input in the variable from A to G.
    """)
    return


@app.cell
def _():
    site_name = chr(65)
    end_site = chr(ord(site_name) + 6)

    for site in range(ord(site_name), ord(end_site)):
        city = chr(site)
        city = input("Enter a city name: ")
        print(f"City name: {city} | Variable name: {chr(site)}")
    return


if __name__ == "__main__":
    app.run()
