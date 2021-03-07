"""
Write a program  to compute and display the sum of the following series:S = (1 + 2) / (1 * 2) + (1 + 2 + 3) / (1 * 2 * 3)
 + --------+ (1 + 2 + 3 + -----+  n ) / (1 * 2 * 3 * -----* n)
"""
from math import prod
n = int(input())
s = 0
for i in range(2,n+1):
    s+= sum(range(1,i+1))/prod(range(1,i+1))
print(s)