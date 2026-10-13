import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Fundamental")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
        Exercise 06: Create a dictionary, add and delete entries, then print its keys, values and items.
    """)
    return


@app.cell
def _():
    info = {"Name": "marimo", "System": "Linux", "Version": 1.0}
    info["License"] = "Apache"
    del info["System"]
    print(f"Keys: {list(info.keys())}")
    print(f"Values: {list(info.values())}")
    for key, value in info.items():
        print(f"{key} -> {value}")
    return


if __name__ == "__main__":
    app.run()
