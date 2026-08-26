import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    fact_num = int(input("Enter a number: "))
    temp = fact_num
    fact = 1

    if fact_num == 0:
        print(f"Factorial of 0 is 1")
    elif fact_num < 0:
        print("Factorial is not defined for negative number")
    else:
        while fact_num >= 1:
            fact *= fact_num
            fact_num -= 1

        print(f"Factorial of {temp} is {fact}")
    return


if __name__ == "__main__":
    app.run()
