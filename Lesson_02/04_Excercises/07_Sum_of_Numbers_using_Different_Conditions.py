import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    nums = int(input("Enter a number"))
    sums = 0

    for i in range(1, nums + 1):
        if i % 2 != 0 and i % 3 != 0 and (i % 5 != 0):
            sums += i

    print(sums)
    return
