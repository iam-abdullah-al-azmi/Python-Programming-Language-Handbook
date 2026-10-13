import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    # Pattern Display
    _user_want = int(input("Enter the no"))

    for _i in range(1, _user_want + 1):
        for _k in range(1, _i + 1):
            print(f"{_k}", end="")

        print()
    return


@app.cell
def _():
    # Pattern Display
    _user_want = int(input("Enter the no"))
    count = 1

    for _i in range(1, _user_want + 1):
        for _k in range(1, _i + 1):
            print(f"{count}", end="")
            count += 1

        print()
    return


@app.cell
def _():
    # Pattern Display
    _user_want = int(input("Enter the no"))

    for _i in range(_user_want, 0, -1):
        for _k in range(1, _i + 1):
            print(f"{_k}", end="")

        print()
    return


@app.cell
def _():
    _user_want = int(input("Enter a number"))
    letter = 65

    for _i in range(1, _user_want + 1):
        for _k in range(1, _i + 1):
            print(f"{chr(letter)}", end="")
            letter += 1

        print()
    return


@app.cell
def _():
    # Hollow Square Pattern
    _user_input = int(input("Enter a number"))

    for _i in range(1, _user_input + 1):
        for _k in range(1, _user_input + 1):
            if _i == 1 or _i == _user_input or _k == 1 or (_k == _user_input):
                print("+", end=" ")
            else:
                print(" ", end=" ")

        print()
    return


@app.cell
def _():
    # Inverted and Rotated Half-Pyramid
    _user_input = int(input("Enter a number"))

    for _i in range(1, _user_input + 1):
        n = _user_input - _i
        for _k in range(1, n + 1):
            print(" ", end=" ")
        for _k in range(1, _i + 1):
            print("+", end=" ")

        print()
    return


@app.cell
def _():
    _user_input = int(input("Enter a number"))

    for _i in range(1, _user_input + 1):
        num_spaces = _user_input - _i
        for _k in range(
            1, num_spaces + 1
        ):  # no of spaces decrease as the row no increases
            print(" ", end=" ")
        num_symbols = 2 * _i - 1
        for _k in range(1, num_symbols + 1):
            print("+", end=" ")

        print()
    return


if __name__ == "__main__":
    app.run()
