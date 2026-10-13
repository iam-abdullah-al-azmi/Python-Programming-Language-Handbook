import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    num = eval(input("Enter a number: "))
    sum_of_digits = 0
    temp_num = num

    while temp_num > 0:
        rem = temp_num % 10
        print(f"Reminder: {rem}", end="|")

        sum_of_digits = sum_of_digits + rem
        print(f"Sum of digits: {sum_of_digits}", end="|")

        temp_num = temp_num // 10
        print(f"Temp: {temp_num}", end="|")

    print(f"Answer: {sum_of_digits}")
    return


if __name__ == "__main__":
    app.run()
