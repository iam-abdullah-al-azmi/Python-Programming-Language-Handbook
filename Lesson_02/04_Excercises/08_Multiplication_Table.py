import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    multiplication_table = int(input("Enter a number"))

    for i in range(1, multiplication_table + 1):
        print(f"Multiplication table of {i}")

        for k in range(1, 11):
            print(i, "*", k, "=", i * k)
    return
