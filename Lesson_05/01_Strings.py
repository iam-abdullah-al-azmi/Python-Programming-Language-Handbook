import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Strings and Lists")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Strings
    A string is a sequence of characters used to store text. You will learn how to create strings, access characters by index, slice them, and use the most common string methods.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Creating strings
    A string is written inside single quotes, double quotes or triple quotes. Triple quotes allow a string to span several lines. `len()` gives the number of characters.
    """)
    return


@app.cell
def _():
    single = 'Hello'
    double = "World"
    multi = """This is
    a multi-line string"""

    print(single, double)
    print(multi)
    print(type(single), len(single))

    return


@app.cell
def _():
    _question = "What is your name?"
    print(_question, type(_question))
    return


@app.cell
def _():
    message = """Tell me about yourself.
    What are the issues you've been facing while learning to code?
    How are you tackling them?
    """
    # For a multiline string we should use triple quotes
    print(message, type(message), len(message))
    return (message,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Indexing
    Every character has a position (index), starting from 0 at the left. Negative indexes count from the right, so `-1` is the last character.
    """)
    return


@app.cell
def _():
    language = "Python"
    print(language[0])
    print(language[3])
    print(language[-1])
    print(language[-3])

    return (language,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Slicing
    `text[start:stop]` gives the characters from `start` up to, but not including, `stop`. Either part can be left out, and a third number sets the step. A step of `-1` walks backwards, which reverses the string.
    """)
    return


@app.cell
def _(language):
    print(language[1:4])
    print(language[2:])
    print(language[:4])
    print(language[::2])
    print(language[::-1])

    return


@app.cell
def _():
    greeting = "hello world"
    for _i in range(11):
        print(greeting[_i], end=" ")
    return (greeting,)


@app.cell
def _(mo):
    mo.md(r"""
    Slicing works on any string, including the multi-line one. Negative positions count from the end, and a slice never goes past the ends of the string.
    """)
    return


@app.cell
def _(message):
    # slicing: string[start:end:step]
    first_message = message[0:24]
    print(first_message)

    back_index_message = message[-114:-1]
    print(back_index_message)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Strings are immutable
    You cannot change a character of an existing string. Trying `language[0] = "J"` raises a `TypeError`. Instead you create a new string.
    """)
    return


@app.cell
def _(language):
    new_language = "J" + language[1:]
    print(new_language)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Joining and repeating
    The `+` operator joins two strings together and `*` repeats a string. The `in` operator checks whether a smaller string is part of a bigger one.
    """)
    return


@app.cell
def _():
    first_name = "Ada"
    last_name = "Lovelace"
    print(first_name + " " + last_name)
    print("-" * 20)
    print("Love" in last_name)
    print("xyz" in last_name)

    return


@app.cell
def _(mo):
    mo.md(r"""
    The `in` operator is case sensitive and gives a bool (`True` or `False`).
    """)
    return


@app.cell
def _(message):
    print("you" in message)
    print("You" in message)
    print(type("You" in message))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Changing the case
    String methods return a new string and leave the original untouched.
    """)
    return


@app.cell
def _():
    sentence = "hello world, welcome to Python"
    print(sentence.upper())
    print(sentence.lower())
    print(sentence.capitalize())
    print(sentence.title())
    print(sentence.swapcase())

    return (sentence,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Searching and counting
    `find()` returns the index of the first match, or `-1` if there is none. `count()` tells how many times a smaller string appears, and `startswith()` / `endswith()` test the beginning and the end.
    """)
    return


@app.cell
def _():
    code = "banana bandana"
    print(code.count("ana"))
    print(code.find("ban"))
    print(code.find("xyz"))
    print(code.startswith("ban"))
    print(code.endswith("ana"))

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Searching from the left and from the right
    `find()` gives the index where the first match starts, counting from the left. `rfind()` searches from the right and gives the index of the last match. A slice that starts at that index returns the rest of the string.
    """)
    return


@app.cell
def _(greeting):
    # the index from which the substring starts, searching from the start
    index = greeting.find("world")
    print(index)
    print(greeting[6:])
    return


@app.cell
def _():
    # the index from which the substring starts, searching from the end
    last_string = "hello world world ML ML, to ML, you ML"
    print(last_string.find("world"))
    print(last_string[6:])
    print(last_string.rfind("world"))
    print(last_string[12:])
    print(last_string.count("world"))
    return (last_string,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Cleaning and replacing
    `strip()` removes spaces (or other characters) from both ends, and `replace()` swaps every match with something else.
    """)
    return


@app.cell
def _(sentence):
    messy = "   some text with spaces   "
    print(f"[{messy.strip()}]")
    print(sentence.replace("world", "Python"))

    return


@app.cell
def _(mo):
    mo.md(r"""
    `replace()` does not change the original string, because strings are immutable. It returns a new string that you must store.
    """)
    return


@app.cell
def _(last_string):
    # replace a substring
    new_string = last_string.replace("ML", "AI/ML")
    print(last_string)  # the main string is not changed
    print(new_string)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Splitting and joining
    `split()` breaks a string into a list of smaller strings, and `join()` does the opposite: it glues a list of strings together using the string it is called on as the separator.
    """)
    return


@app.cell
def _(sentence):
    words = sentence.split()
    print(words)

    csv_line = "red,green,blue"
    print(csv_line.split(","))
    print("-".join(words))

    return


@app.cell
def _(mo):
    mo.md(r"""
    By default `split()` splits on spaces and returns a list. A separator can be given, and `type()` confirms the result is a list.
    """)
    return


@app.cell
def _():
    _prompt = "This is a string"
    tokens = _prompt.split()  # by default split by space and it returns a list
    print(tokens, type(tokens))

    dashed_prompt = "This-is-a-string"
    dashed_tokens = dashed_prompt.split("-")
    print(dashed_tokens)
    return


@app.cell
def _(mo):
    mo.md(r"""
    To split by two different separators, first replace one of them with the other and then split once.
    """)
    return


@app.cell
def _():
    mixed_prompt = "This is-a string, split by both space and -"
    mixed_tokens = mixed_prompt.split("-")  # this will split only by "-"
    print(mixed_tokens)

    # to solve this we can first replace "-" with " " and then split by space
    mixed_tokens = mixed_prompt.replace("-", " ").split()
    print(mixed_tokens)
    return (mixed_tokens,)


@app.cell
def _(mixed_tokens):
    # join() glues the list back together using any separator
    joined_sentence = "^<->^".join(mixed_tokens)
    print(joined_sentence, type(joined_sentence))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Looping over a string
    A `for` loop visits one character at a time, which makes it easy to count or test characters.
    """)
    return


@app.cell
def _(sentence):
    vowel_count = 0
    for _ch in sentence:
        if _ch in "aeiou":
            vowel_count += 1
    print(f"Vowels in the sentence: {vowel_count}")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Checking the kind of characters
    Methods that start with `is` return `True` or `False`.
    """)
    return


@app.cell
def _():
    print("abc".isalpha(), "abc123".isalpha())
    print("2025".isdigit(), "20a5".isdigit())
    print("HELLO".isupper(), "hello".islower())

    return


if __name__ == "__main__":
    app.run()
