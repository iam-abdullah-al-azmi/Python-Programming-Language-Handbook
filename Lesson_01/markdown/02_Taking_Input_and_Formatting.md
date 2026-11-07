---
title: Python Basics
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Taking Input and Formatting
In this notebook you will read values typed by the user with the input function, convert them to numbers, and format numbers and text neatly with the format function.
<!---->
## Taking user input
The input function shows a message and returns what the user typed. The code below is commented out because it waits for the keyboard; remove the `#` to try it.

```python {.marimo}
# length = int(input("Enter the length: "))
# breadth = int(input("Enter the breadth: "))

# area = length * breadth
# print("The area of the rectangle is:", area)
```

- When using the input function, the input is taken as a string by default. To convert it to an integer, we use the int() function. If we want to take float input, we can use the float() function and others accordingly.

- To get an expected input, we can use the eval() function. For example, if we want to take a list as input, we can use eval(input()). Be careful: eval runs whatever is typed, so use it only with input you trust.

```python {.marimo}
# number = eval(input("Enter a number: "))
# strings = input("Enter a string: ")

# print(number, type(number))
# print(strings, type(strings))
```

The next cell imitates what input returns by using a string directly. Notice that the value is text until we convert it.

```python {.marimo}
typed = "25"  # this is what input() would return
print(typed, type(typed))
as_int = int(typed)
as_float = float(typed)
print(as_int + 5, as_float + 5)
```

## Formatting with the format function
The format function returns a string. The second argument is a format specifier that says how the value must look.

```python {.marimo}
x = 34.44456968
x = format(x, ".3f")  # This will round the number to 3 decimal places
print(x, type(x))
```

```python {.marimo}
y = 34.44456968
y = format(
    y, "7.3f"
)  # This will round the number to 3 decimal places and make the total length 7 by adding spaces in the front if necessary
print(y, len(y), type(y))
print(" " in y)
print(f"{y.find(' ')}")
```

```python {.marimo}
z = 20.345123
z = format(
    z, "<7.3f"
)  # This will round the number to 3 decimal places and make the total length 7 by adding spaces in the back if necessary
print(z, len(z))
```

```python {.marimo}
from math import pi

print(pi, format(pi, ".3%"), type(pi))
```

## Specifier format

- '10.2f' ---> floating point number with precision 2 and width 10.
- '<10.2f' ---> Left justify the floating point number.
- '>10.2f' ---> Right justify the formatted item.
- '10X' ---> Format integer in hexadecimal with width 10
- '20s' ---> Format string with width 20
- '10.2%' ---> Format the number as a percentage

```python {.marimo}
val = 344
print(format(val, "10X"))
```

```python {.marimo}
characters = "characters"
print(format(characters, ".5s"), format(characters, "5s"))
print(len(characters))
```

## Number systems
The same format function can show an integer in binary (`b`), octal (`o`) and hexadecimal (`x` or `X`).

```python {.marimo}
num = 255
print(format(num, "b"), format(num, "o"), format(num, "x"), format(num, "X"))
```

## f-strings
An f-string puts values directly inside the text using curly braces, and accepts the same format specifiers after a colon.

```python {.marimo}
name = "Azmi"
price = 1234.5678
print(f"{name} paid ${price:.2f}")
print(f"[{name:<10}] [{name:>10}] [{price:>12.1f}]")
```