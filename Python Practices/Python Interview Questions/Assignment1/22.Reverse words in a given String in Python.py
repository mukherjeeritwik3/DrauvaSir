"""
We are given a string and we need to reverse words of a given string?

Examples:

Input : str = geeks quiz practice code
Output : str = code practice quiz geeks
"""

def reverseString(s):
    words = s.split(' ')
    return ' '.join(reversed(words))

print(reverseString('hello my world'))