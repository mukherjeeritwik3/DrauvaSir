# Compound Interest

"""
Formula to calculate compound interest annually is given by:

A = P*(1 + R/100)**t
Compound Interest = A – P
Where,
A is amount
P is principle amount
R is the rate and
T is the time span
"""


def compoundInterest(p, r, t):
    a = p*pow((1 + (r / 100)),t)
    cI = a - p
    return cI


print(compoundInterest(10000, 10.25, 5))
