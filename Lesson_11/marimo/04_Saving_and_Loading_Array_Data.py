import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="NumPy Operations")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Saving and Loading Array Data
    Learn how to write array data to a text file, read it back with `genfromtxt`, filter rows by a condition, and save arrays with `savetxt` and in NumPy's own `.npy` format.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Creating a data file
    The data file `shear_cutting_info.txt` is created inside a temporary folder so that nothing is left behind. It has a header line (`Name,ID,Time`) followed by 21 rows.
    """)
    return


@app.cell
def _():
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

    return Path, path, workspace


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Reading with genfromtxt
    `np.genfromtxt` loads a text file into an array. With `names=True` the first line is used as the column names and `dtype=None` lets NumPy detect the type of every column, which gives a structured array whose columns are reached by name.
    Without a header use `np.genfromtxt(path, delimiter=",")` instead (or `skip_header=1` to skip it).
    """)
    return


@app.cell
def _(np, path):
    data = np.genfromtxt(path, delimiter=",", names=True, dtype=None, encoding="utf-8")
    print(data.ndim, data.size, data.shape, data.dtype.names)
    print(data["ID"])

    return (data,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Filtering rows
    A boolean mask keeps only the rows we want. Here the rows where `ID` is zero are removed, and `count_nonzero` counts the zeros.
    """)
    return


@app.cell
def _(data, np):
    print(np.count_nonzero(data["ID"] == 0))
    mask = data["ID"] != 0
    filtered = data[mask]
    print(filtered.size)

    return (filtered,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Saving with savetxt
    `np.savetxt` writes a 2D array to a text file. `delimiter` separates the values, `fmt` sets the number format and `header` adds a first line.
    """)
    return


@app.cell
def _(data, filtered, np, path):
    _table = np.column_stack([filtered[_name] for _name in data.dtype.names])
    saved_path = path.with_name("filtered.csv")
    np.savetxt(saved_path, _table, delimiter=",", fmt="%d", header=",".join(data.dtype.names), comments="")
    print(saved_path.read_text()[:60])
    print(np.loadtxt(saved_path, delimiter=",", skiprows=1).shape)

    return (saved_path,)


@app.cell
def _(mo):
    mo.md(r"""
    ## The .npy format
    `np.save` and `np.load` store an array in NumPy's binary format, which keeps the shape and data type exactly.
    """)
    return


@app.cell
def _(np, saved_path):
    _array = np.arange(6).reshape(2, 3)
    _npy_path = saved_path.with_name("array.npy")
    np.save(_npy_path, _array)
    _loaded = np.load(_npy_path)
    print(_loaded, _loaded.dtype, np.array_equal(_array, _loaded))
    return


@app.cell
def _(path, workspace):
    workspace.cleanup()  # delete the temporary folder
    print(path.exists())
    return


if __name__ == "__main__":
    app.run()
