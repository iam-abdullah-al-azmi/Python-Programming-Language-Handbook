---
title: Exceptions, Files and Modules Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 04: Create a small module file in a temporary folder with a function, import it, and call the function. Delete the temporary files afterwards.

```python {.marimo hide_code="true"}
import importlib
import os
import shutil
import sys
import tempfile

_folder = tempfile.mkdtemp()
with open(os.path.join(_folder, "exercise_04_helper.py"), "w") as _file:
    _file.write("def square(n):\n")
    _file.write("    return n * n\n")

sys.path.insert(0, _folder)
helper = importlib.import_module("exercise_04_helper")
print(helper.square(7))

sys.path.remove(_folder)
sys.modules.pop("exercise_04_helper", None)
shutil.rmtree(_folder)
```