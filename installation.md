# Installation

---

## Overview

To install Python, the specific guidelines for both Windows have been provided below. For Linux Operating System (OS) it already comes pre-installed. Also, apart from installing Python, we also need to create virtual environment to install necessary packages in an isolated systems. Guidlines for this also provided below.

---

## Installation Steps

- Open PowerShell in Windows Terminal and install Python:

```bash
winget install Python.Python.3.12
```

- Close and reopen PowerShell, then verify Python is installed:

```bash
python --version
```

---

## Virtual Environment

### Windows

### Linux

- First, create a virtual environment using:

```bash
python3.12 -m venv .venv
```

- Then, activate it using:

```bash
.venv/bin/activate
```

- Lastly, run:

```bash
pip install -r requirements.txt
```

to install all the required packages.
