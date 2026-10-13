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
        Excercise 03: Calculate the total price of a product given its price and quantity. Use the formatting to properly display the outputs.
    """)


@app.cell
def _():
    price = 1234.5678
    product = "Laptop"
    quantity = 5

    print(f"Product: {product:<15} | Price: ${price:>8.2f} | Quantity: {quantity:>3}")
    print(
        "Product: {:<15} | Price: ${:>8.2f} | Quantity: {:>3}".format(
            product, price, quantity
        )
    )
    print("Total: ${:.2f}".format(price * quantity))
    return


if __name__ == "__main__":
    app.run()
