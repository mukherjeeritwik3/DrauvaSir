"""
Given a character, we need to print its ASCII value in C/C++/Java/Python.

Examples :

Input : a
Output : 97

Input : D
Output : 68
"""


def ascii(x):
    value = ord(x)
    return value

print(ascii('D'))