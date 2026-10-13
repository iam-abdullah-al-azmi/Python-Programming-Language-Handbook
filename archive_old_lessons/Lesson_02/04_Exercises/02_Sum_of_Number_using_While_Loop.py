import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    div_num = int(input("Enter a number: "))
    sum_of_num = 0

    while div_num > 0:
        if div_num % 5 == 0:
            sum_of_num += div_num
        div_num -= 1

    print(sum_of_num)
    return


if __name__ == "__main__":
    app.run()
