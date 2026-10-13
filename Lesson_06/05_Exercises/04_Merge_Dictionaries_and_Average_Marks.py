import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Tuples, Sets and Dictionaries")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 04: Merge two dictionaries into a new one (the value from the second dictionary wins for a repeated key), then use a dictionary of student marks to print the average mark of one student with two decimal places.
    """)
    return


@app.cell
def _():
    first = {"a": 1, "b": 2, "c": 3}
    second = {"c": 30, "d": 40}
    merged = {}
    for key, value in first.items():
        merged[key] = value
    for key, value in second.items():
        merged[key] = value
    print(merged)
    print(merged == first | second)
    return


@app.cell
def _():
    student_marks = {
        "Krishna": [67, 68, 69],
        "Arjun": [70, 98, 63],
        "Malika": [52, 56, 60],
    }
    query_name = "Malika"
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print(f"{query_name}: {average:.2f}")
    return


if __name__ == "__main__":
    app.run()
