import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    print("Number from 1 to 10 reverse order:")

    for i in range(10, 0, -1):
        print(i, end=" ")
    return


if __name__ == "__main__":
    app.run()
