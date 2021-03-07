# Write programs  to print theseries:0,1,1,2,4,7.......n  terms

n = int(input())
a = 0
b = 1
c =1
print(a)
print(b)
for i in range(1,n+1):
    temp = c
    print(c)
    c = a+b+c
    a =b
    b = temp