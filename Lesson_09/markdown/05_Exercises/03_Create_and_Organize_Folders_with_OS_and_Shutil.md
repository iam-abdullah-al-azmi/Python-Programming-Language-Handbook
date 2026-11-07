---
title: Exceptions, Files and Modules Exercises
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

Exercise 03: Inside a temporary folder create a folder called reports, write a text file into it, copy the file to a new file name, list the folder, check the file size and finally delete the whole temporary folder.

```python {.marimo hide_code="true"}
import os
import shutil
import tempfile

_workspace = tempfile.mkdtemp()
_reports = os.path.join(_workspace, "reports")
os.makedirs(_reports)

_original = os.path.join(_reports, "january.txt")
with open(_original, "w") as _file:
    _file.write("Sales: 100\n")

_copy = os.path.join(_reports, "january_backup.txt")
shutil.copy(_original, _copy)

print(sorted(os.listdir(_reports)))
print(os.path.isfile(_copy), os.path.getsize(_copy), "bytes")

shutil.rmtree(_workspace)
print("Workspace removed:", not os.path.exists(_workspace))
```