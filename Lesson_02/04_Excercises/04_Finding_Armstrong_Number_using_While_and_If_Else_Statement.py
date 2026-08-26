import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    arm_num = int(input("Enter a number: "))
    original_num = arm_num
    original_num_2 = arm_num
    arm_sum = 0
    point = 0

    while arm_num > 0:
        _rem = arm_num % 10
        point += 1
        arm_num = arm_num // 10

    while original_num > 0:
        _rem = original_num % 10
        arm_sum += _rem**point
        original_num = original_num // 10

    if arm_sum == original_num_2:
        print(f"{original_num_2} is a armstrong number")
    else:
        print(point)
        print(f"{original_num_2} is not a armstrong number")
    return


if __name__ == "__main__":
    app.run()
