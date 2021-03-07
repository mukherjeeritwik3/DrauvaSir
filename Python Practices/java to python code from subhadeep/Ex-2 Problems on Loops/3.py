"""
3.Write programs  to find the sum of the given series:1 + (1/2!)  + (1/3!) + (1/4!) + .......... + (1/n!)
"""
def fact(a):
    return 1 if a==0 else a*fact(a-1)
s = 0
n = int(input())
for i in range(1,n+1):
    if i==1:
        s+= fact(i)
    else:
        s+= 1/fact(i)
print(s)