import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    perfect_num = int(input("Enter a number: "))
    perfect_sum = 0

    for _i in range(1, perfect_num):
        if perfect_num % _i == 0:
            perfect_sum += _i

    if perfect_num == perfect_sum:
        print(f"{perfect_num} is a perfect number")
    else:
        print(f"{perfect_num} is not a perfect number")
    return


if __name__ == "__main__":
    app.run()
