---
title: NumPy Operations
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Saving and Loading Array Data
Learn how to write array data to a text file, read it back with `genfromtxt`, filter rows by a condition, and save arrays with `savetxt` and in NumPy's own `.npy` format.
<!---->
## Creating a data file
The data file `shear_cutting_info.txt` is created inside a temporary folder so that nothing is left behind. It has a header line (`Name,ID,Time`) followed by 21 rows.

```python {.marimo}
import tempfile
from pathlib import Path

workspace = tempfile.TemporaryDirectory()
path = Path(workspace.name) / "shear_cutting_info.txt"

try:
    with open(path, "w+") as _file:
        _file.write(",".join(["Name", "ID", "Time"]) + "\n")
        _data = [f"{k},{k},{k}" for k in range(21)]
        _file.write("\n".join(_data))
except OSError:
    print("OS Error")
except Exception as _e:
    print(f"{_e}")

print(path.read_text()[:60])
```

```python {.marimo}
import numpy as np
```

## Reading with genfromtxt
`np.genfromtxt` loads a text file into an array. With `names=True` the first line is used as the column names and `dtype=None` lets NumPy detect the type of every column, which gives a structured array whose columns are reached by name.
Without a header use `np.genfromtxt(path, delimiter=",")` instead (or `skip_header=1` to skip it).

```python {.marimo}
data = np.genfromtxt(path, delimiter=",", names=True, dtype=None, encoding="utf-8")
print(data.ndim, data.size, data.shape, data.dtype.names)
print(data["ID"])
```

## Filtering rows
A boolean mask keeps only the rows we want. Here the rows where `ID` is zero are removed, and `count_nonzero` counts the zeros.

```python {.marimo}
print(np.count_nonzero(data["ID"] == 0))
mask = data["ID"] != 0
filtered = data[mask]
print(filtered.size)
```

## Saving with savetxt
`np.savetxt` writes a 2D array to a text file. `delimiter` separates the values, `fmt` sets the number format and `header` adds a first line.

```python {.marimo}
_table = np.column_stack([filtered[_name] for _name in data.dtype.names])
saved_path = path.with_name("filtered.csv")
np.savetxt(saved_path, _table, delimiter=",", fmt="%d", header=",".join(data.dtype.names), comments="")
print(saved_path.read_text()[:60])
print(np.loadtxt(saved_path, delimiter=",", skiprows=1).shape)
```

## The .npy format
`np.save` and `np.load` store an array in NumPy's binary format, which keeps the shape and data type exactly.

```python {.marimo}
_array = np.arange(6).reshape(2, 3)
_npy_path = saved_path.with_name("array.npy")
np.save(_npy_path, _array)
_loaded = np.load(_npy_path)
print(_loaded, _loaded.dtype, np.array_equal(_array, _loaded))
```

```python {.marimo}
workspace.cleanup()  # delete the temporary folder
print(path.exists())
```