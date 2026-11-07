---
title: Functions
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Defining and Calling Functions
A function is a named block of code that you write once and run whenever you need it. In this notebook you will learn how to define a function with `def`, call it, and give it parameters, including default values.
<!---->
## Defining a function and calling it
A function is defined with the `def` keyword, a name, parentheses holding its parameters, and a colon. The indented lines below it are the body. Nothing runs until the function is called by writing its name followed by parentheses.

```python {.marimo}
def greet_language(lang):
    print(f"Welcome to the World of {lang}")


greet_language("Python")
```

The value you pass when calling (`"Python"`) is called an **argument**, and the name in the definition (`lang`) is called a **parameter**. You can call the same function as many times as you like with different arguments.

```python {.marimo}
greet_language("C++")
greet_language("Perl")
```

## Default arguments
A parameter can be given a default value. If the caller does not pass anything for it, the default is used. If the caller does pass a value, it replaces the default.

```python {.marimo}
def greet_default(lang="C++"):
    print(f"Welcome to the World of {lang}")


greet_default()
greet_default("Perl")
```

## Several parameters and positional arguments
A function can take any number of parameters. When you call it, the arguments are matched to the parameters by **position**, so the order matters.

```python {.marimo}
def show_values(a, b, c):
    print(f"a={a} | b={b} | c={c}")


show_values(10, 20, 30)
show_values(30, 20, 10)
```

## Keyword arguments
If you write the parameter name along with the value, you do not have to care about the position any more. This is called a **keyword argument**.

```python {.marimo}
show_values(b=10, c=20, a=30)
```

## A function that prints instead of returning
The function below only prints the result. It does not hand anything back to the caller, so Python gives back the special value `None`. Trying to use that result in a calculation causes an error. The next notebook shows how `return` solves this.

```python {.marimo}
def sqr_summation(a, b, c):
    summation = a**2 + b**2 + c**2
    print(f"Summation of {a}, {b} and {c} is {summation}")


result = sqr_summation(10, 20, 30)
print(result)

# result + 10 would raise a TypeError because None cannot be added to an integer
```