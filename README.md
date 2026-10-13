# Python Programming Language Handbook

![Python x marimo](python-marimo-banner.jpg)

## Overview

This repository is a self-study Python course for people who want to learn on their own. It has 15 lessons, from `print()` to data visualization. Every lesson has four lesson notebooks and four exercises.

The lessons are [marimo](https://marimo.io/) notebooks instead of plain Python files. marimo is a newer Python notebook that addresses limitations of the Jupyter Notebook. So, along with learning the Python programming language, you also learn how to get started with marimo notebooks.

## Who this is for

Anyone who wants to learn Python from the beginning and has no programming experience. The lessons start with printing text and end with data analysis and charts.

## Prerequisites

- A recent version of Python 3, from [python.org](https://www.python.org/downloads/).
- A code editor such as Visual Studio Code, or just a terminal and a web browser.

## Setup

1. Clone or download this repository.
2. Install the packages used by the notebooks:

```bash
pip install -r requirements.txt
```

3. Open any notebook in the marimo editor, for example:

```bash
marimo edit Lesson_01/01_Printing_Output.py
```

To run a notebook as a read-only app instead, use `marimo run <file>`.

## Course structure

The course follows the order of the [GeeksforGeeks Python tutorial](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/): Basics, Functions, Data Structures, OOP Concepts, Exception Handling, File Handling, Packages or Libraries, and Data Science. The detailed list of every notebook and exercise is in [SYLLABUS.md](SYLLABUS.md).

| Lesson | Topic                                                                                        |
| ------ | -------------------------------------------------------------------------------------------- |
| 01     | [Python Basics](SYLLABUS.md#lesson-01-python-basics)                                         |
| 02     | [Conditionals and Loops](SYLLABUS.md#lesson-02-conditionals-and-loops)                       |
| 03     | [Functions](SYLLABUS.md#lesson-03-functions)                                                 |
| 04     | [Functional Tools and Generators](SYLLABUS.md#lesson-04-functional-tools-and-generators)     |
| 05     | [Strings and Lists](SYLLABUS.md#lesson-05-strings-and-lists)                                 |
| 06     | [Tuples, Sets and Dictionaries](SYLLABUS.md#lesson-06-tuples-sets-and-dictionaries)          |
| 07     | [Classes and Objects](SYLLABUS.md#lesson-07-classes-and-objects)                             |
| 08     | [OOP Principles](SYLLABUS.md#lesson-08-oop-principles)                                       |
| 09     | [Exceptions, Files and Modules](SYLLABUS.md#lesson-09-exceptions-files-and-modules)          |
| 10     | [NumPy Foundations](SYLLABUS.md#lesson-10-numpy-foundations)                                 |
| 11     | [NumPy Operations](SYLLABUS.md#lesson-11-numpy-operations)                                   |
| 12     | [Pandas Foundations](SYLLABUS.md#lesson-12-pandas-foundations)                               |
| 13     | [Pandas Data Cleaning and Analysis](SYLLABUS.md#lesson-13-pandas-data-cleaning-and-analysis) |
| 14     | [Matplotlib Visualization](SYLLABUS.md#lesson-14-matplotlib-visualization)                   |
| 15     | [Seaborn and Plotly Visualization](SYLLABUS.md#lesson-15-seaborn-and-plotly-visualization)   |

## Repository layout

Each lesson has its own folder, and every lesson folder has the same shape, so you always know where to look.

```text
Python-Programming-Language-Handbook/
|-- README.md
|-- SYLLABUS.md              the full list of lessons, notebooks and exercises
|-- requirements.txt         Python packages used by the notebooks
|-- LICENSE
|-- Lesson_01/               one folder per lesson, Lesson_01 to Lesson_15
|   |-- 01_Printing_Output.py
|   |-- 02_Taking_Input_and_Formatting.py
|   |-- 03_Variables_and_Data_Types.py
|   |-- 04_Operators_and_Math_Functions.py
|   `-- 05_Exercises/         four exercises that practise this lesson
|-- ...
`-- Lesson_15/               data files used by a lesson sit next to its notebooks
```

## How to use this course

1. Go through the lessons in order, from Lesson 01 to Lesson 15. Later lessons use what earlier lessons teach.
2. In each lesson, open the four notebooks in numbered order and run the cells as you read.
3. Change the code and run it again. Experimenting is the fastest way to learn.
4. Do the four exercises in the lesson's `05_Exercises` folder. Each exercise has a description and a worked solution; try it yourself before you read the solution.

Notebooks that read data files (Lessons 12 to 15) find them next to the notebook, so run them from inside this repository.

## Contributing

Found a mistake or want to improve a lesson? Open an issue or a pull request.

## License

This project is licensed under the terms in the [LICENSE](LICENSE) file.

## Acknowledgements

- The structure of this README (overview, prerequisites, repository layout, how to use the course, and a separate syllabus file) follows the example of the [ReDI School of Digital Integration introduction-to-python course](https://github.com/ReDI-Aarhus/introduction-to-python).
- The order of the lessons follows the [GeeksforGeeks Python Programming Language Tutorial](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/).
