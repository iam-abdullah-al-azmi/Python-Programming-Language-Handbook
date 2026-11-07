---
title: Python Basics Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Calculate the total price of a product given its price and quantity. Use the formatting to properly display the outputs.

```python {.marimo hide_code="true"}
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
```