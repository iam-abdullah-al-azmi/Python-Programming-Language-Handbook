---
title: Tuples, Sets and Dictionaries
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Dictionaries
A dictionary stores data as key-value pairs and lets us look a value up by its key. In this notebook you will create dictionaries, read and change their values and compare them.
<!---->
## Creating a dictionary
There are several ways to create a dictionary: curly brackets with `key: value` pairs, an empty dictionary that is filled later, the `dict()` function with keyword arguments, or `dict()` with a list of key-value tuples.

```python {.marimo}
dic = {"name": "Abdullah Al Azmi", "age": 24, "city": "Dhaka", "country": "Bangladesh"}
print(dic, type(dic))

information = {"Name": "VSCode", "System": "Linux"}
print(information)

information_1 = {}
information_1["Name"] = "Cursor"
information_1["System"] = "Linux"
print(information_1)

information_2 = dict(Name="Helix", System="Linux")
print(information_2)

information_3 = dict([("Name", "CodeBlock"), ("System", "Linux")])
print(information_3)
```

## Accessing values
We read a value with its key in square brackets. The `get()` method does the same, but returns `None` (or a default value we choose) instead of raising a `KeyError` when the key is missing. The default value is not stored in the dictionary, so we must pass it every time we call `get()`.

```python {.marimo}
print(dic.keys())
print(f"Name: {dic['name']}, Age: {dic['age']}, City: {dic['city']}, Country: {dic['country']}")
print(information_3["Name"], information_3.get("Name"))

print(dic.get("learning"))
print(dic.get("learning", 0))  # default value
print(dic.get("learning", "Python"))  # default value
print(dic.get("learning"))  # still None, the default was not saved
```

## Adding and replacing values
Assigning to a key replaces its value if the key exists and adds a new pair if it does not. `update()` can add or replace several pairs at once. A key is unique, so a duplicate key in the literal is overwritten by the last value.

```python {.marimo}
dic["age"] = 25  # replace
print(dic)

dic["learning"] = "Python"  # add
print(dic)

dic.update({"OS": "Linux"})
print(dic)
dic.update({"GUI": "Gnome", "Kernel": 6.18})
print(dic)

duplicate_dic = {"name": "Abdullah Al Azmi", "age": 24, "name": "Phitron"}
print(duplicate_dic)  # the last value of the duplicate key wins
```

## Deleting values
- `del` removes a key and raises a `KeyError` if it is missing, so use it when we are sure that the key is present.
- `pop()` removes a key and returns its value. It can also take a default value, which avoids the error when the key is missing.

```python {.marimo}
info = dict(Name="Zed", System="Linux", Version=1.0, License="MIT")

del info["System"]
print(info)

removed = info.pop("Version")
print(removed, info)

print(info.pop("Missing", "not found"))
```

## Keys must be immutable
A dictionary key has to be hashable, so immutable types such as strings, numbers and tuples are allowed, but a list is not.

```python {.marimo}
try:
    bad_dic = {[1, 2, 3]: "Phitron"}
except TypeError as error:
    print(f"TypeError: {error}")

good_dic = {(1, 2, 3): "Phitron"}
print(good_dic)
```

## Looping through a dictionary
Looping over a dictionary directly gives its keys. The `items()` method gives each key-value pair as a tuple, which we can unpack in the loop.

```python {.marimo}
for _key in information:
    print(_key, end=" | ")
print()

for _key, _value in dic.items():
    print(_key, _value, end=" | ")
```

## Comparing dictionaries
Two dictionaries are equal when they have the same key-value pairs, no matter in which order the pairs were written.

```python {.marimo}
information_one = dict(Name="Zed", System="Linux")
information_two = dict(System="Linux", Name="Zed")

print(information_one == information_two)
print(information_one != information_two)
```

## Formatting a string with a dictionary
The `%` formatting style can take the values straight from a dictionary using the key names.

```python {.marimo}
information_5 = dict(Name="Zed", System="Linux")
text = "This is %(Name)s for %(System)s system." % information_5
print(text)
```