"""
Print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till n-th term.


Examples:

Input : n = 5
Output : 225
13 + 23 + 33 + 43 + 53 = 225

Input : n = 7
Output : 784
13 + 23 + 33 + 43 + 53 +
63 + 73 = 784

"""
#Simple Method - slow method
"""
def cubicNatural(n):
    sum = 0
    for i in range(1,n+1):
        sum+= i*i*i
    return sum

print(cubicNatural(5))
"""

#Time Complexity : O(n) Method

"""
An efficient solution is to use direct mathematical formula which is (n ( n + 1 ) / 2) ^ 2
For n = 5 sum by formula is
       (5*(5 + 1 ) / 2)) ^ 2
          = (5*6/2) ^ 2
          = (15) ^ 2
          = 225

For n = 7, sum by formula is
       (7*(7 + 1 ) / 2)) ^ 2
          = (7*8/2) ^ 2
          = (28) ^ 2
          = 784
"""
def fastCubicnatural(n):
    sum = (n*(n+1)/2)
    return int(sum*sum)

print(fastCubicnatural(5))