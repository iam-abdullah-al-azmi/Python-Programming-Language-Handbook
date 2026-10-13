import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Tuples, Sets and Dictionaries Exercises")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exercise 03: Count how many times each word appears in a sentence using a dictionary, then print its keys, values and items.
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
    return (frequency,)


@app.cell
def _(frequency):
    print(f"Keys: {list(frequency.keys())}")
    print(f"Values: {list(frequency.values())}")
    for key, value in frequency.items():
        print(f"{key} -> {value}")
    return


if __name__ == "__main__":
    app.run()
