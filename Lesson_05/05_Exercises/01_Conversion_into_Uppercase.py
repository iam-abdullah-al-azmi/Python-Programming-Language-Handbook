import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Strings and Lists")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    Exercise 01: Take the string 'hello world' and print it in upper case, in title case, reversed, and the number of times the letter 'o' appears in it.
    """)
    return


@app.cell
def _():
    text = "hello world"
    print(text.upper())
    print(text.title())
    print(text[::-1])
    print(f"Number of 'o': {text.count('o')}")

    return


if __name__ == "__main__":
    app.run()
