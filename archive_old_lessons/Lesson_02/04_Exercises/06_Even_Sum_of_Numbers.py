import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    ev_num = int(input("Enter a number:"))
    ev_sum = 0

    for _i in range(1, ev_num + 1):
        if _i % 2 == 0:
            ev_sum += _i

    print(f"Even sum is {ev_sum}")
    return


if __name__ == "__main__":
    app.run()
