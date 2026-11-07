---
title: Conditionals and Loops
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# While Loops
In this notebook you will repeat code as long as a condition holds using the while loop, work with the digits of a number, and stop a loop with break.
<!---->
## Sum of the numbers from 0 to 10
A while loop checks its condition before every round. We must change the variable inside the loop, otherwise the loop never ends.

```python {.marimo}
num = 0
sum_of_num = 0

while num <= 10:
    sum_of_num += num
    print(num, end="|")
    num += 1

print(num)
print("Sum:", sum_of_num)
```

## Printing characters with ASCII codes
Given the character "A", print the characters from A to G using the ASCII code and a while loop instead of typing them manually.

```python {.marimo}
ascii_code = ord("A")
end_code = ascii_code + 6
while ascii_code <= end_code:
    print(f"Character: {chr(ascii_code)} | ASCII code: {ascii_code}")
    ascii_code += 1
```

## Factorial
The factorial of n is 1 * 2 * ... * n. We also use if, elif and else to handle 0 and negative numbers. The original version of this example read the number with `int(input("Enter a number: "))`.

```python {.marimo}
fact_num = 5  # fact_num = int(input("Enter a number: "))
temp = fact_num
fact = 1

if fact_num == 0:
    print("Factorial of 0 is 1")
elif fact_num < 0:
    print("Factorial is not defined for negative number")
else:
    while fact_num >= 1:
        fact *= fact_num
        fact_num -= 1

    print(f"Factorial of {temp} is {fact}")
```

## Working with the digits of a number
`num % 10` gives the last digit and `num // 10` removes it. Repeating these two steps visits every digit. This cell finds the sum of digits and prints each step.

```python {.marimo}
_num = 1234  # _num = eval(input("Enter a number: "))
_sum_of_digits = 0
_temp_num = _num

while _temp_num > 0:
    _rem = _temp_num % 10
    print(f"Remainder: {_rem}", end="|")

    _sum_of_digits = _sum_of_digits + _rem
    print(f"Sum of digits: {_sum_of_digits}", end="|")

    _temp_num = _temp_num // 10
    print(f"Temp: {_temp_num}", end="|")

print(f"Answer: {_sum_of_digits}")
```

## Sum of the digits in reversed order
Building a new number with `reversed * 10 + digit` reverses the digits.

```python {.marimo}
_temp_num = 12345
_reversed = 0
while _temp_num > 0:
    _rem = _temp_num % 10
    _reversed = _reversed * 10 + _rem
    _temp_num = _temp_num // 10
print(_reversed)
```

## Printing the digits of a number in reverse
Print the last digit, then remove it, and repeat until nothing is left. The `end=" "` argument keeps the digits on one line.

```python {.marimo}
# _number = int(input())   # for example: 4567
_number = 4567

while _number > 0:
    print(_number % 10, end=" ")
    _number = _number // 10
```

## Reversing the digits for several numbers
A while loop can sit inside a for loop to handle several numbers one after another. The special case 0 is handled first, because the while loop would not run for it. The original problem reads the number of test cases and then each number from the keyboard.

```python {.marimo}
# _tests = int(input())
_tests = 3

for _case in range(_tests):
    # _number = int(input())
    _number = _case * 1234  # gives 0, 1234 and 2468
    if _number == 0:
        print(0)
        continue
    while _number > 0:
        print(_number % 10, end=" ")
        _number = _number // 10
    print()
```

## Predict the output: break in a while loop
The loop stops as soon as `_i` becomes 2, but the line after the loop still runs.

```python {.marimo}
_i = 0
while _i < 3:
    _i = _i + 1
    if _i == 2:
        break
print("Done")
```

## Sum of multiples of 5
Add every number from the given number down to 1 that is divisible by 5.

```python {.marimo}
_div_num = 50
_sum_of_num = 0
while _div_num > 0:
    if _div_num % 5 == 0:
        _sum_of_num += _div_num
    _div_num -= 1
print(_sum_of_num)
```

## Armstrong number
An Armstrong number equals the sum of its digits each raised to the power of the number of digits, for example 153 = 1**3 + 5**3 + 3**3. The first loop counts the digits and the second one adds the powers.

```python {.marimo}
_arm_num = 153
_original = _arm_num
_remaining = _arm_num
_arm_sum = 0
_point = 0

while _arm_num > 0:
    _point += 1
    _arm_num = _arm_num // 10

while _remaining > 0:
    _rem = _remaining % 10
    _arm_sum += _rem**_point
    _remaining = _remaining // 10

if _arm_sum == _original:
    print(f"{_original} is an armstrong number")
else:
    print(f"{_original} is not an armstrong number")
```

## Infinite loop with break
`while True` repeats forever, so we need break to leave. This pattern is useful when asking the user for input until it is valid.

```python {.marimo}
_count = 0
while True:
    _count += 1
    if _count * _count > 50:
        break
print("First number whose square is above 50:", _count)

# while True:
#     answer = input("Type 'yes' to stop: ")
#     if answer == "yes":
#         break
```