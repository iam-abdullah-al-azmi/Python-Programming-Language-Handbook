import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    temp_num = eval(input("Enter a number: "))
    sum_of_reversed = 0

    while temp_num > 0:
        rem = temp_num % 10
        sum_of_reversed = sum_of_reversed * 10 + rem
        temp_num = temp_num // 10

    print(sum_of_reversed)
    return


if __name__ == "__main__":
    app.run()
