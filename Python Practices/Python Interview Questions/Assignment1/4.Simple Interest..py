# Simple Interest formula: SI = P*R*T/100
"""
principle = int(input("Input Principle"))
rate = float(input("input rate of interest"))
time = int(input("enter the time "))

simpleInterest = (principle*rate*time)/100

print("THe Simple interest is ",simpleInterest)

"""

def simpleInterest(p,r,t):
    si = (p*r*t)/100
    return si


print(simpleInterest(4500,9.5,6))