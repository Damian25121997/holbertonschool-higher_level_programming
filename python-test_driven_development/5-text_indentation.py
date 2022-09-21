#!/usr/bin/python3
"""Define the print a text with 2 new lines after each
of these characters: . , ? and :
"""


def text_indentation(text):
    """Function print a text with 2 new lines after each
    of these characters: . , ? and :.
    Args:
        text: is a text.
    Return:
        Always.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end="")
