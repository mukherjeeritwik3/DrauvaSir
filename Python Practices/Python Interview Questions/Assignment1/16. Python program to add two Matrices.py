"""
Aim : Program to compute the sum of two matrices and then print it in Python.
Examples:

Input :
 X= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

Output :
 result= [[10,10,10],
         [10,10,10],
         [10,10,10]]
"""

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

b = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

result = [[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j]+b[i][j]
print(result)
