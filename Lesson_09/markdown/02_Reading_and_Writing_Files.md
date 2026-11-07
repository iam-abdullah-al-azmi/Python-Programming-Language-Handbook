---
title: Exceptions, Files and Modules
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Reading and Writing Files
Learn how to open a text file in Python, read it in different ways, and write or append text using the file modes `r`, `w`, `w+` and `a+`.
<!---->
## Reading a file
`open(path, "r")` opens a file in read mode (the default mode when nothing is mentioned).
`read()` returns the whole content as one string. The file is `sample.txt`, which lives next to this notebook.

```python {.marimo}
from pathlib import Path

path = Path(__file__).resolve().parent / "sample.txt"
_file = open(path, "r")  # file open in read mode only, if we don't mention anything this is the default mode
_content = _file.read()
print(_content, type(_content))
```

`readlines()` returns a list with one string per line. A file opened by hand must be closed with `close()`.

```python {.marimo}
_file = open(path, "r")
_content = _file.readlines()
print(_content, type(_content))
print(_file.closed)
_file.close()
print(_file.closed)
```

## The with statement
When we use the `with` statement we don't have to worry about closing the file; Python closes it automatically.

```python {.marimo}
with open(path, "r") as _file:
    _content = _file.readlines()
    print(_content, type(_content))
print(_file.closed)
```

## Reading line by line
A file can be used directly in a `for` loop. Every line already ends with a new line character, so `print` adds a blank line. Use `end=""` or `strip()` to avoid it.

```python {.marimo}
with open(path, "r") as _file:
    for _line in _file:
        print(_line)
```

```python {.marimo}
with open(path, "r") as _file:
    for _line in _file:
        print(_line, end="")
```

```python {.marimo}
with open(path, "r") as _file:
    for _line in _file:
        _stripped = _line.strip()
        print(_stripped)
```

## Writing a file
The examples below write to a temporary folder so that nothing is left behind next to the notebook.

- `"w"` opens the file in write mode: if the file already exists it is overwritten.
- `write()` does not add a new line by itself, so the three lines below end up joined together.

```python {.marimo}
import tempfile

workspace = tempfile.mkdtemp()
out_path = Path(workspace) / "test.txt"

with open(out_path, "w") as _file:
    _file.write("Hello test file line 1.")
    _file.write("Hello test file line 2.")
    _file.write("Hello test file line 3.")

with open(out_path, "r") as _file:
    print(_file.read(), end="")
```

`"w+"` allows writing and reading at the same time. After writing, `seek(0)` moves the cursor back to the start of the file so that we can read from the beginning.

```python {.marimo}
with open(out_path, "w+") as _file:
    _file.write("Hello test file with write plus read mode line 1.")
    _file.write("Hello test file with write plus read mode line 2.")
    _file.write("Hello test file with write plus read mode line 3.")
    _file.seek(0)
    print(_file.read(), end="")
```

`"a+"` opens the file in append mode: instead of overwriting the file, new text is added at the end. The `+` also lets us read.

```python {.marimo}
with open(out_path, "a+") as _file:
    _file.write("Hello test 2 file.")
    _file.write("Hello test 2 file.")
    _file.write("Hello test 2 file.")
    _file.seek(0)
    print(_file.read(), end="")
```

## Putting it together
Write lines with `\n`, read them back, remove the new line characters with `strip()` (using `map`) and keep only the long lines (using `filter`).

```python {.marimo}
with open(out_path, "a+") as _file:
    _file.write("\nNew Line ONE\n")
    _file.write("New Line TWO\n")
    _file.write("New Line THREE\n")
    _file.write("New Line FOUR\n")
    _file.seek(0)
    _content = _file.readlines()
    print(f"Content of the file: \n{_content}\n")
    _content = list(map(str.strip, _content))  # removing the new line characters using the strip() function
    print(f"Content of the mapped file for removing new line: \n{_content}\n")
    _filtered_content = list(filter(lambda val: len(val) > 15, _content))
    print(f"Filtered Content of the file for length greater than 15: \n{_filtered_content}")
```

```python {.marimo}
import shutil

shutil.rmtree(workspace)  # clean up the temporary folder
print(Path(workspace).exists())
```