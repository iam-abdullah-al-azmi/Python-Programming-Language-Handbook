---
title: Matplotlib Visualization
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Styling Line Plots
This notebook shows how to read data from a CSV file and make a line plot readable with a legend, colors, line width, line style, markers and a grid.
<!---->
## Reading the Data
We use pandas to read the yearly enrollment of two courses from a CSV file. The path is built relative to this notebook.

```python {.marimo}
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent / "enrollment_data.csv")
df
```

## Plotting Two Columns
Each column of the DataFrame is plotted against the year. The `label` argument gives every line a name.

```python {.marimo}
plt.plot(df["Year"], df["Programming"], label="Programming")
plt.plot(df["Year"], df["Digital Marketing"], label="Digital Marketing")
plt.gca()
```

## Adding a Legend
The labels are only shown when `plt.legend()` is called.

```python {.marimo}
plt.plot(df["Year"], df["Programming"], label="Programming")
plt.plot(df["Year"], df["Digital Marketing"], label="Digital Marketing")

plt.legend()
plt.gca()
```

## Changing the Color
The `color` argument accepts color names or hex codes.

```python {.marimo}
plt.plot(df["Year"], df["Programming"], label="Programming", color="#32a852")
plt.plot(
    df["Year"],
    df["Digital Marketing"],
    label="Digital Marketing",
    color="#8b32a8",
)

plt.legend()
plt.gca()
```

## Changing the Line Width
The `linewidth` argument controls how thick a line is.

```python {.marimo}
plt.plot(
    df["Year"],
    df["Programming"],
    label="Programming",
    color="#32a852",
    linewidth=5,
)
plt.plot(
    df["Year"],
    df["Digital Marketing"],
    label="Digital Marketing",
    color="#8b32a8",
    linewidth=5,
)

plt.legend()
plt.gca()
```

## Changing the Line Style
The `linestyle` argument selects between solid, dashed (`"dashed"`), dash-dot (`"dashdot"`) and dotted (`"dotted"`) lines.

```python {.marimo}
plt.plot(
    df["Year"], df["Programming"], label="Programming", linestyle="dashdot"
)
plt.plot(
    df["Year"],
    df["Digital Marketing"],
    label="Digital Marketing",
    linestyle="dotted",
)

plt.legend()
plt.gca()
```

## Adding Markers
The `marker` argument marks every data point. `"o"` draws a circle.

```python {.marimo}
plt.plot(
    df["Year"],
    df["Programming"],
    label="Programming",
    linestyle="dashdot",
    marker="o",
)
plt.plot(
    df["Year"],
    df["Digital Marketing"],
    label="Digital Marketing",
    linestyle="dotted",
    marker="o",
)

plt.legend()
plt.gca()
```

## Putting It All Together with a Grid
`plt.grid()` draws grid lines behind the plot. Each line can have its own style, and passing `linewidth=None` simply keeps the default width.

```python {.marimo}
plt.plot(
    df["Year"],
    df["Programming"],
    label="Programming",
    linestyle="dashdot",
    marker="o",
    linewidth=3,
)
plt.plot(
    df["Year"],
    df["Digital Marketing"],
    label="Digital Marketing",
    linestyle="dotted",
    marker="o",
    linewidth=None,
)

plt.grid()
plt.legend()
plt.gca()
```