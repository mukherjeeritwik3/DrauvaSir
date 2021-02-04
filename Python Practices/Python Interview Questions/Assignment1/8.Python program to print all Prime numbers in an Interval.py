"""
Given two positive integers start and end. The task is to write a Python program to print all Prime numbers in an Interval.
Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
The first few prime numbers are {2, 3, 5, 7, 11, ….}.

The idea to solve this problem is to iterate the val from start to end using a for loop and for every number, if it is
greater than 1, check if it divides n. If we find any other number which divides, print that value.
"""


# Hard Question need to Understand More
def primeRangeprint(start, end):
    for i in range(start, end):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                print(i)


primeRangeprint(11, 25)
