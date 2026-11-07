---
title: Conditionals and Loops
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# If-Else Statements
In this notebook you will make your programs take decisions with if, elif and else, combine conditions with logical operators, and use nested conditions.
<!---->
## The if statement
An if statement runs its indented block only when the condition is True. The block is defined by indentation.

```python {.marimo}
temperature = 32
if temperature > 30:
    print("It is a hot day")
print("This line always runs")
```

## if and else
else runs when the condition is False.

```python {.marimo}
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

## elif
When there are more than two possibilities, use elif (else if). Python checks the conditions from top to bottom and runs only the first block whose condition is True.

```python {.marimo}
score = 76
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"
print(f"Score: {score} | Grade: {grade}")
```

## Conditions with logical operators
Use and, or and not to build a condition from smaller ones.

```python {.marimo}
year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

## Nested if
An if statement can be placed inside another one. The inner condition is checked only if the outer condition is True.

```python {.marimo}
age = 25
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Please show an ID")
else:
    print("Too young")
```

## Minimum and maximum of three numbers
Compare the first number with the others one by one, keeping the biggest (or smallest) seen so far. This is a classic competitive programming (ICPC) problem.

```python {.marimo}
# user_input = input()   # for example: 7 3 9
# numbers = user_input.split()
# _num_1 = int(numbers[0])
# _num_2 = int(numbers[1])
# _num_3 = int(numbers[2])
num_1 = 7
num_2 = 3
num_3 = 9

max_num = num_1

if num_2 > max_num:
    max_num = num_2
if num_3 > max_num:
    max_num = num_3

min_num = num_1

if num_2 < min_num:
    min_num = num_2
if num_3 < min_num:
    min_num = num_3

print(min_num, max_num)
```

## Predict the output
Read the code and decide what it prints before you run it. Only the first condition that is true runs, and the rest are skipped.

```python {.marimo}
x = 5
if x > 3:
    print("A")
elif x > 1:
    print("B")
else:
    print("C")
```

## Taking the number from the user
The same checks work with a number typed by the user. The following code is commented out because it waits for the keyboard.

The factorial example from the old version of this lesson uses a loop, so it appears in the While Loops notebook.

```python {.marimo}
# value = int(input("Enter a number: "))
# if value > 0:
#     print("Positive")
# elif value < 0:
#     print("Negative")
# else:
#     print("Zero")
```

## Conditional expression
A short if-else can be written on one line: `value_if_true if condition else value_if_false`.

```python {.marimo}
y = 10
label = "even" if y % 2 == 0 else "odd"
print(y, "is", label)
```