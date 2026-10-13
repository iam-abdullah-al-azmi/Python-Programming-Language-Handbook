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
        Exercise 05: Count how many times each word appears in a sentence using a dictionary.
    """)
    return


@app.cell
def _():
    sentence = "the cat and the dog and the bird"
    frequency = {}
    for word in sentence.split():
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    print(frequency)
    return


if __name__ == "__main__":
    app.run()
