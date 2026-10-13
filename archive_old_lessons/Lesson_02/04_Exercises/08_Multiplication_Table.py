import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    multiplication_table = int(input("Enter a number"))

    print(f"Multiplication table of {multiplication_table}")

    for i in range(1, 11):
        print(multiplication_table, "*", i, "=", multiplication_table * i)
    return
