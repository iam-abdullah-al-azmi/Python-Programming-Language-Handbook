---
title: Python Basics
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Operators and Math Functions
In this notebook you will learn the arithmetic, relational, logical, bitwise and assignment operators, and use the math module and the ord and chr functions.
<!---->
## Arithmetic operators
`+` addition, `-` subtraction, `*` multiplication, `/` division (always a float), `//` floor division, `%` remainder and `**` power.

```python {.marimo}
a = 17
b = 5
print(a + b, a - b, a * b)
print(a / b, a // b, a % b, a**b)
```

## Assignment operators
`+=`, `-=`, `*=`, `/=`, `//=`, `%=` and `**=` update a variable using its current value.

```python {.marimo}
c = 10
c += 5
print(c)
c *= 2
print(c)
c //= 4
print(c)
c **= 2
print(c)
```

## Relational operators
Relational operators compare two values and give a bool: `==`, `!=`, `<`, `>`, `<=` and `>=`.

```python {.marimo}
x = 17
y = 5
print(x == y, x != y, x < y, x > y, x <= 17, y >= 6)
```

## Logical operators
`and`, `or` and `not` combine boolean values. `and` is True only if both sides are True, `or` is True if at least one side is True.

```python {.marimo}
age = 21
print(age > 18 and age < 30)
print(age < 18 or age == 21)
print(not age > 18)
```

## Bitwise operators
Bitwise operators work on the binary digits of integers: `&` and, `|` or, `^` xor, `~` not, `<<` shift left and `>>` shift right.

```python {.marimo}
p = 12  # 1100
q = 10  # 1010
print(p & q, p | q, p ^ q, ~p)
print(p << 2, p >> 2)
print(format(p & q, "04b"), format(p | q, "04b"))
```

## Operator summary
Arithmetic: `+ - * / // % **`. Relational: `== != <= >= < >`. Logical: `and not or`. Bitwise: `& | ~ ^ << >>`.

Python also has built-in numeric functions that need no import: abs, round, pow, min, max, divmod.

```python {.marimo}
print(abs(-7), round(3.14159, 2), round(2.5), pow(2, 10))
print(min(4, 9, 1), max(4, 9, 1), divmod(17, 5))
```

## The math module
To use mathematical functions we import the math module.

- ceil(x) ----> Round x up to the nearest integer and return that integer.
- floor(x) ----> Returns the largest integer not greater than x
- exp(x) ----> Returns the exponential value e^x
- log(x) ----> Returns the natural logarithm of x (to base e)
- log(x, base) ----> Returns the logarithm of x to the given base
- sqrt(x) ----> Return the square root of x
- sin(x) ----> Return the sine of x, where x is the value in radians
- asin(x) ----> Return the angle in radians whose sine is x
- cos(x) ----> Return the cosine of x, where x is the value in radians
- acos(x) ----> Return the angle in radians whose cosine is x
- tan(x) ----> Return the tangent of x, where x is the value in radians
- degrees(x) ----> Convert angle x from radians to degrees
- radians(x) ----> Convert angle x from degrees to radians

```python {.marimo}
import math

print(math.ceil(10.23))
print(math.floor(10.23))
print(math.exp(2))
print(format(math.exp(2), ".3f"))
print(math.log(2.7))
print(math.floor(math.log(2.7)))
print(math.ceil(math.log(2.7)))
```

```python {.marimo}
print(math.sqrt(144), math.log(8, 2), math.pi)
print(math.sin(math.radians(30)), math.cos(0), math.tan(math.radians(45)))
print(math.degrees(math.pi), math.degrees(math.asin(1)), math.degrees(math.acos(0)))
```

## ord and chr functions

- "ord" returns the ASCII (Unicode) value of a character
- "chr" returns the character of an ASCII value

```python {.marimo}
print(ord("A"), chr(65))
print(ord("a") - ord("A"), chr(ord("A") + 2))
```