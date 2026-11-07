---
title: Functional Tools and Generators
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Lambda Functions
A lambda function is a small, anonymous function written in a single line. You will learn its syntax, how it compares with a regular `def` function, and when it is useful.
<!---->
## Syntax
A lambda is special, anonymous and inline: `lambda parameters: expression`. There can be many parameters but only one expression, and the value of that expression is returned automatically, so there is no `return` keyword.

```python {.marimo}
sqr_sum = lambda x, y: x**2 + y**2
print(sqr_sum(2, 3))
```

The lambda above does exactly the same thing as this regular function.

```python {.marimo}
def sqr_sum_def(x, y):
    return x**2 + y**2


print(sqr_sum_def(2, 3))
```

## Lambdas that return a True or False answer
A lambda can contain a comparison. This is very common because tools such as `filter()` (next notebook) need small yes/no functions.

```python {.marimo}
chk_even = lambda x: x % 2 == 0
print(chk_even(10))
print(chk_even(11))
```

## Conditions and default values
A lambda can use a one-line conditional expression, and its parameters can have default values just like a normal function.

```python {.marimo}
bigger = lambda a, b: a if a > b else b
print(bigger(7, 12))

add_ten = lambda value, extra=10: value + extra
print(add_ten(5))
print(add_ten(5, 20))
```

## Calling a lambda immediately
Because a lambda is an expression, you can also write it in brackets and call it on the spot without giving it a name.

```python {.marimo}
print((lambda x, y: x * y)(6, 7))
```

## Passing a lambda to another function
The real strength of a lambda is passing it as an argument to a function that expects another function. The built-in `sorted()` accepts a `key` function that decides what to compare. Here the words are sorted by their length.

```python {.marimo}
words = ["banana", "fig", "cherry", "kiwi"]
print(sorted(words, key=lambda word: len(word)))
```