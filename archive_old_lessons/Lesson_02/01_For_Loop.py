import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    num = 0
    sum_of_num = 0

    while num <= 10:
        sum_of_num += num
        print(num, end="|")
        num += 1

    print(num)
    return


if __name__ == "__main__":
    app.run()
