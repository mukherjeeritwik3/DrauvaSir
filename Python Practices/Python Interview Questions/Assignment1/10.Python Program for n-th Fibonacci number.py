"""
A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms. This means to say the
nth term is the sum of (n-1)th and (n-2)th term.
"""

a = 10
n1= 0
n2 = 1
print(n1)
print(n2)
prev = 0
for i in range(1,a):
    temp=n2
    n2+= prev
    print(n2)
    prev = temp