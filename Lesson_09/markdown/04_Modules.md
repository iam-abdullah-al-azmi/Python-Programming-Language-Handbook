---
title: Exceptions, Files and Modules
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Modules
Learn how to reuse code with modules: import your own Python file and the modules that ship with Python.
<!---->
## What is a module
A module is simply a Python file. Anything defined in it (functions, variables) can be used in another file with `import`.
This notebook uses `something_in_file.py`, which sits next to it and defines a function `greeting` and a dictionary `person`.
Importing a module runs its code once, which is why the dictionary is printed when the import happens.

```python {.marimo}
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # make sure Python can find the file next to this notebook

import something_in_file as info

info.greeting(" Azmi")
```

## Using the names inside a module
Use `module.name` to reach anything the module defines. `as` gives the module a shorter alias.

```python {.marimo}
print(info.person)
print(info.person[0])
```

## Standard library modules
Python comes with many ready-made modules. `import math` loads the whole module, while `from math import sqrt` loads just one name that can then be used without the prefix.

```python {.marimo}
import math
from math import sqrt

print(math.pi)
print(math.ceil(4.2), math.factorial(5))
print(sqrt(49))
```

`dir(module)` lists everything a module offers.

```python {.marimo}
import random

random.seed(1)  # a seed makes the "random" numbers repeatable
print(random.randint(1, 10))
print([name for name in dir(random) if not name.startswith("_")][:5])
```