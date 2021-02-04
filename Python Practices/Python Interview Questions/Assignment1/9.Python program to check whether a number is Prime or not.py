"""
Given a positive integer N, The task is to write a Python program to check if the number is prime or not.
Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
The first few prime numbers are {2, 3, 5, 7, 11, ….}.
Examples :


Input:  n = 11
Output: true

Input:  n = 15
Output: false

Input:  n = 1
Output: false
"""
## Problem questions
def primeCheck(x):
    if x>1:
        for i in range(2,x):
            if(x%i)==0:
                break
            else:
                print( "It is Prime")

        print("not prime")
primeCheck(9)