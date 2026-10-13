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
        Exercise 03: Given a dictionary of student marks, print the average mark of a queried student with two decimal places.
    """)
    return


@app.cell
def _():
    student_marks = {"Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60]}
    query_name = "Malika"
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print(f"Average of {query_name}: {average:.2f}")
    return


if __name__ == "__main__":
    app.run()
