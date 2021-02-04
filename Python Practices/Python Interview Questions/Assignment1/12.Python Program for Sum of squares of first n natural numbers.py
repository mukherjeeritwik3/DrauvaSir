"""
Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.

Examples:

Input : N = 4
Output : 30
12 + 22 + 32 + 42
= 1 + 4 + 9 + 16
= 30

Input : N = 5
Output : 55
"""

# O(n) Method - SLower method
"""
def sumSquarenatural(n):
    sum =0
    for i in range(1,n+1):
        sum+= i*i
    return sum

print(sumSquarenatural(4))

"""
# O(1) Method - Faster Method

"""
Sum of squares of first N natural number = (N*(N+1)*(2*N+1))/6

For Example

For N = 4, Sum = (4*(4+1)*(2*4+1))/6
               = (4*5*9)/6
               = 180/6
               = 30

For N = 5, Sum = (5*(5+1)*(2*5+1))/6
               = (5*6*11)/6
               = 55
"""

def sumSquareNaturalSpeed(n):
    sum = (n*(n+1)*(2*n+1))/6
    return sum

print(int(sumSquareNaturalSpeed(4)))