---
title: Matplotlib Visualization
marimo-version: 0.25.2
width: medium
---

```python {.marimo}
import marimo as mo
```

# Scatter Plots and Histograms
In this notebook you will use scatter plots to see how two variables are related and histograms to see how the values of one variable are distributed.

```python {.marimo}
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

iq_df = pd.read_csv(Path(__file__).resolve().parent / "student_IQdata.csv")
iq_df
```

## Scatter Plot
`plt.scatter(x, y)` draws one dot per row. It is used to check whether two variables are related. Here more study hours tend to go with a higher IQ score.

```python {.marimo}
plt.xlabel("Study Hours")
plt.ylabel("IQ Score")
plt.title("Relation between Study Hours and IQ Score")
plt.scatter(iq_df["Study_Hour"], iq_df["IQ_Score"])

plt.grid()
plt.gca()
```

## A Scatter Plot Without a Clear Pattern
When two variables are not related, the dots form no pattern. Shoe size has no obvious relation with the IQ score.

```python {.marimo}
plt.xlabel("Shoe Size")
plt.ylabel("IQ Score")
plt.title("Relation between Shoe Size and IQ Score")
plt.scatter(iq_df["Shoe_Size"], iq_df["IQ_Score"])

plt.grid()
plt.gca()
```

## Changing the Marker
The `marker` argument changes the shape of the dots. Here `"x"` is used.

```python {.marimo}
plt.xlabel("Chilling Hours")
plt.ylabel("IQ Score")
plt.title("Relation between Chilling Hours and IQ Score")
plt.scatter(iq_df["Chilling_Hours"], iq_df["IQ_Score"], marker="x")

plt.grid()
plt.gca()
```

## Histogram
`plt.hist()` splits the values into ranges called bins and counts how many values fall into each bin.

```python {.marimo}
plt.xlabel("IQ Score")
plt.ylabel("Frequency")
plt.title("Frequency of IQ Score among Students")
plt.hist(iq_df["IQ_Score"])
plt.grid()
plt.gca()
```

```python {.marimo}
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.title("Frequency of Study Hours among Students")
plt.hist(iq_df["Study_Hour"])
plt.grid()
plt.gca()
```

## Changing the Number of Bins
The `bins` argument sets how many bins to use, and `edgecolor` draws a border around each bar so that the bars are easy to tell apart.

```python {.marimo}
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.title("Frequency of Study Hours among Students")
plt.hist(iq_df["Study_Hour"], bins=15, edgecolor="#f7fcf8")
plt.grid()
plt.gca()
```

## Custom Bin Edges
Instead of a number, `bins` can be a list of bin edges.

```python {.marimo}
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.title("Frequency of Study Hours among Students")
plt.hist(iq_df["Study_Hour"], bins=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
plt.grid()
plt.gca()
```