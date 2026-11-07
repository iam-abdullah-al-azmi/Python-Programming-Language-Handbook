---
title: Exceptions, Files and Modules
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# OS and Shutil
Learn how to work with files and folders from Python using the `os` and `shutil` modules.

## The os and shutil modules
- The `os` module lets Python talk to the operating system: build paths, list folders, create and remove files and folders.
- The `shutil` module works on top of `os` and handles high-level file operations such as copying, moving and deleting a whole folder.
- Both modules come with Python, so nothing has to be installed.
<!---->
Useful os functions
- os.getcwd() ----> Returns the current working directory
- os.listdir(path) ----> Returns the names of the files and folders inside a folder
- os.mkdir(path) ----> Creates a single folder
- os.makedirs(path, exist_ok=True) ----> Creates a folder along with any missing parent folders
- os.path.join(a, b) ----> Joins path parts using the correct separator for the operating system
- os.path.exists(path) ----> Returns True if the file or folder exists
- os.path.isfile(path) / os.path.isdir(path) ----> Checks whether the path is a file or a folder
- os.path.getsize(path) ----> Returns the size of a file in bytes
- os.rename(old, new) ----> Renames a file or a folder
- os.remove(path) ----> Deletes a file
- os.rmdir(path) ----> Deletes an empty folder

```python {.marimo}
import os
import tempfile

# We work inside a temporary folder so that nothing is left behind in the repository
workspace = tempfile.mkdtemp()
print(f"Workspace: {workspace}")
print(f"Current working directory: {os.getcwd()}")
```

```python {.marimo}
# Creating folders and files
notes_folder = os.path.join(workspace, "notes")
os.makedirs(os.path.join(notes_folder, "archive"), exist_ok=True)

note_path = os.path.join(notes_folder, "note.txt")
with open(note_path, "w") as _file:
    _file.write("Python is fun!\n")

print(os.listdir(notes_folder))
print(os.path.exists(note_path), os.path.isfile(note_path), os.path.isdir(notes_folder))
print(f"Size of note.txt: {os.path.getsize(note_path)} bytes")
```

```python {.marimo}
# Renaming and deleting
renamed_path = os.path.join(notes_folder, "renamed_note.txt")
os.rename(note_path, renamed_path)
print(os.listdir(notes_folder))

os.remove(renamed_path)
os.rmdir(os.path.join(notes_folder, "archive"))
print(os.listdir(notes_folder))
```

Useful shutil functions
- shutil.copy(src, dst) ----> Copies a file to a file or a folder
- shutil.copytree(src, dst) ----> Copies a whole folder with everything inside it
- shutil.move(src, dst) ----> Moves a file or a folder
- shutil.rmtree(path) ----> Deletes a folder together with everything inside it (os.rmdir only works on an empty folder)

```python {.marimo}
import shutil

source_folder = os.path.join(workspace, "source")
os.makedirs(source_folder)
with open(os.path.join(source_folder, "data.txt"), "w") as _file:
    _file.write("some data\n")

# Copy a single file
shutil.copy(os.path.join(source_folder, "data.txt"), os.path.join(workspace, "data_copy.txt"))

# Copy a whole folder
shutil.copytree(source_folder, os.path.join(workspace, "backup"))

# Move a file into another folder
shutil.move(os.path.join(workspace, "data_copy.txt"), os.path.join(workspace, "backup"))

print(sorted(os.listdir(workspace)))
print(sorted(os.listdir(os.path.join(workspace, "backup"))))
```

```python {.marimo}
# Cleaning up: rmtree removes the folder even when it is not empty
shutil.rmtree(workspace)
print(os.path.exists(workspace))
```